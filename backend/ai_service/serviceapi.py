from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

#installar requisitos: pip install -r requirements.txt
#arrancar servidor: uvicorn serviceapi:app --reload --port 8001 
# Rutas a los modelos entrenados
NUDGING_MODEL_PATH = "models/nudging_model.pkl"
ACCESSIBILITY_MODEL_PATH = "models/accessibility_model.pkl"
RISK_MODEL_PATH = "models/risk_model.pkl"

app = FastAPI(
    title="AI Service - Inclusive Banking Demo",
    description="Servicio de IA para nudging, perfil de accesibilidad y riesgo transaccional",
    version="1.0.0",
)

# ---------- Carga de modelos ----------
nudging_model = None
accessibility_model = None
risk_model = None

if os.path.exists(NUDGING_MODEL_PATH):
    nudging_model = joblib.load(NUDGING_MODEL_PATH)

if os.path.exists(ACCESSIBILITY_MODEL_PATH):
    accessibility_model = joblib.load(ACCESSIBILITY_MODEL_PATH)

if os.path.exists(RISK_MODEL_PATH):
    risk_model = joblib.load(RISK_MODEL_PATH)


# ---------- Esquemas Pydantic ----------

# 1) NUDGING (detección de dificultad)


class NudgingFeatures(BaseModel):
    user_id: Optional[str] = Field(None, description="ID de usuario (opcional)")
    session_id: Optional[str] = Field(None, description="ID de sesión (opcional)")
    screen: str = Field(..., description="Nombre de la pantalla, ej. 'send-money'")
    num_validation_errors: int = Field(..., ge=0)
    time_on_screen_seconds: int = Field(..., ge=0)
    num_back_navigations: int = Field(..., ge=0)
    steps_total: int = Field(..., ge=1)
    current_step: int = Field(..., ge=1)


class NudgingPrediction(BaseModel):
    needs_help: bool
    difficulty_score: float
    recommended_nudge_type: Literal["assist", "info", "warning"]
    reason: str


class NudgingResponse(BaseModel):
    user_id: Optional[str]
    session_id: Optional[str]
    screen: str
    model_version: str
    result: NudgingPrediction


# 2) PERFIL DE ACCESIBILIDAD


class AccessibilityFeatures(BaseModel):
    user_id: Optional[str] = None
    can_read_small_text: bool
    uses_screen_reader: bool
    feels_confident_with_apps: Literal["low", "medium", "high"]
    age_range: Literal["18_30", "31_50", "51_60", "60_plus"]
    avg_time_per_screen_seconds: int = Field(..., ge=0)
    total_validation_errors: int = Field(..., ge=0)
    requested_help_count: int = Field(..., ge=0)


class AccessibilityRecommendation(BaseModel):
    theme: Literal["standard-accessible", "large-text-high-contrast", "voice-assisted"]
    screen_reader_mode: bool
    font_scale: float
    nudging_level: Literal["low", "medium", "high"]
    voice_feedback: bool


class AccessibilityResponse(BaseModel):
    user_id: Optional[str]
    model_version: str
    recommendation: AccessibilityRecommendation
    confidence: float
    explanation: List[str]


# 3) RIESGO / FRAUDE


class RiskFeatures(BaseModel):
    user_id: Optional[str] = None
    amount: float
    is_new_beneficiary: bool
    hour_of_day: int = Field(..., ge=0, le=23)
    num_past_transactions: int = Field(..., ge=0)
    avg_transaction_amount: float
    max_transaction_amount: float
    num_transactions_to_beneficiary: int = Field(..., ge=0)
    is_new_device: bool
    geolocation_changed: bool


class RiskResult(BaseModel):
    risk_level: Literal["low", "medium", "high"]
    risk_score: float
    risk_factors: List[str]


class RiskResponse(BaseModel):
    user_id: Optional[str]
    model_version: str
    result: RiskResult


origins = [
    "http://localhost:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# ---------- Endpoints ----------


@app.get("/ai/health", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "models": {
            "nudging_loaded": nudging_model is not None,
            "accessibility_loaded": accessibility_model is not None,
            "risk_loaded": risk_model is not None,
        },
    }


@app.post("/ai/nudge", response_model=NudgingResponse, tags=["nudging"])
def ai_nudge(payload: NudgingFeatures):
    """
    Evalúa si la persona usuaria probablemente necesita ayuda en una pantalla.
    """
    if nudging_model is None:
        # Fallback: regla simple, por si el modelo no está cargado
        needs_help = (
            payload.num_validation_errors >= 2
            or payload.time_on_screen_seconds > 60
        )
        difficulty_score = 0.5 if needs_help else 0.1
    else:
        X = [[
            payload.num_validation_errors,
            payload.time_on_screen_seconds,
            payload.num_back_navigations,
            payload.steps_total,
            payload.current_step,
        ]]
        pred = nudging_model.predict(X)[0]
        needs_help = bool(pred)
        # Podemos simular un score con la probabilidad del árbol
        if hasattr(nudging_model, "predict_proba"):
            proba = nudging_model.predict_proba(X)[0][1]
            difficulty_score = float(proba)
        else:
            difficulty_score = 0.7 if needs_help else 0.2

    # Tipo de nudge según dificultad
    if difficulty_score > 0.75:
        n_type = "assist"
        reason = "high_error_rate_or_time"
    elif difficulty_score > 0.4:
        n_type = "info"
        reason = "moderate_difficulty"
    else:
        n_type = "warning"  # advertencias suaves, por ejemplo sobre seguridad
        reason = "low_difficulty"

    return NudgingResponse(
        user_id=payload.user_id,
        session_id=payload.session_id,
        screen=payload.screen,
        model_version="nudging-v1.0",
        result=NudgingPrediction(
            needs_help=needs_help,
            difficulty_score=round(difficulty_score, 2),
            recommended_nudge_type=n_type,  # en tu app puedes usar solo "assist" si quieres
            reason=reason,
        ),
    )


@app.post("/ai/accessibility", response_model=AccessibilityResponse, tags=["accessibility"])
def ai_accessibility(payload: AccessibilityFeatures):
    """
    Recomienda un perfil de accesibilidad (tema, tamaño de letra, voz, nivel de nudging).
    Si el usuario ya seleccionó manualmente un tema, se respeta.
    """
    feels_map = {"low": 0, "medium": 1, "high": 2}
    age_map = {"18_30": 0, "31_50": 1, "51_60": 2, "60_plus": 3}

    X = [[
        int(payload.can_read_small_text),
        int(payload.uses_screen_reader),
        feels_map[payload.feels_confident_with_apps],
        age_map[payload.age_range],
        payload.avg_time_per_screen_seconds,
        payload.total_validation_errors,
        payload.requested_help_count,
    ]]

    # Fallback con lógica extendida
    if accessibility_model is not None:
        theme = str(accessibility_model.predict(X)[0])
    else:
        # ⚙️ Ajuste de reglas más rico
        if payload.uses_screen_reader:
            theme = "voice-assisted"
        elif (not payload.can_read_small_text) or payload.age_range in ["51_60", "60_plus"]:
            theme = "large-text-high-contrast"
        elif payload.feels_confident_with_apps == "low":
            theme = "large-text-high-contrast"
        else:
            theme = "standard-accessible"

    font_scale = 1.6 if theme == "large-text-high-contrast" else 1.2
    nudging_level = "high" if payload.requested_help_count >= 2 else "medium"
    screen_reader_mode = payload.uses_screen_reader
    voice_feedback = payload.uses_screen_reader or nudging_level == "high"

    explanation = []
    if payload.uses_screen_reader:
        explanation.append("User uses screen reader, enabling voice-assisted mode")
    elif not payload.can_read_small_text or payload.age_range in ["51_60", "60_plus"]:
        explanation.append("Increased font and contrast for readability")
    elif payload.feels_confident_with_apps == "low":
        explanation.append("Low confidence detected, enabling more accessible theme")
    else:
        explanation.append("Standard accessible mode applied")

    return AccessibilityResponse(
        user_id=payload.user_id,
        model_version="accessibility-v1.1",
        recommendation=AccessibilityRecommendation(
            theme=theme,
            screen_reader_mode=screen_reader_mode,
            font_scale=font_scale,
            nudging_level=nudging_level,
            voice_feedback=voice_feedback,
        ),
        confidence=0.9,
        explanation=explanation,
    )

@app.post("/ai/risk", response_model=RiskResponse, tags=["risk"])
def ai_risk(payload: RiskFeatures):
    X = [[
        payload.amount,
        int(payload.is_new_beneficiary),
        payload.hour_of_day,
        payload.num_past_transactions,
        payload.avg_transaction_amount,
        payload.max_transaction_amount,
        payload.num_transactions_to_beneficiary,
        int(payload.is_new_device),
        int(payload.geolocation_changed),
    ]]

    if risk_model is not None:
        risk_level_pred = risk_model.predict(X)[0]
        risk_level = str(risk_level_pred)
        if hasattr(risk_model, "predict_proba"):
            proba = risk_model.predict_proba(X)[0]
            risk_score = float(max(proba))
        else:
            risk_score = 0.7 if risk_level != "low" else 0.3
    else:
        score = 0.0
        if payload.amount > payload.avg_transaction_amount * 2:
            score += 1.5
        if payload.is_new_beneficiary:
            score += 1.5
        if payload.hour_of_day < 6 or payload.hour_of_day > 22:
            score += 1.0
        if payload.is_new_device:
            score += 1.0
        if payload.geolocation_changed:
            score += 1.0

        if score <= 1.0:
            risk_level = "low"
        elif score <= 3.0:
            risk_level = "medium"
        else:
            risk_level = "high"
        risk_score = min(score / 5.0, 1.0)

    risk_factors = []
    if payload.amount > payload.avg_transaction_amount * 2:
        risk_factors.append("AMOUNT_MUCH_HIGHER_THAN_AVERAGE")
    if payload.is_new_beneficiary:
        risk_factors.append("NEW_BENEFICIARY")
    if payload.hour_of_day < 6 or payload.hour_of_day > 22:
        risk_factors.append("UNUSUAL_TIME")
    if payload.is_new_device:
        risk_factors.append("NEW_DEVICE")
    if payload.geolocation_changed:
        risk_factors.append("LOCATION_CHANGED")
    if payload.num_past_transactions < 3:
        risk_factors.append("LOW_HISTORY")

    return RiskResponse(
        user_id=payload.user_id,
        model_version="risk-v1.0",
        result=RiskResult(
            risk_level=risk_level,  # type: ignore
            risk_score=round(risk_score, 2),
            risk_factors=risk_factors,
        ),
    )