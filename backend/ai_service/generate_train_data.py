import random
import csv
from datetime import datetime


def generate_nudging_data(n_rows=300, filename="nudging_training.csv"):
    """
    Datos sintéticos para detectar dificultad de uso (nudging).
    """
    fieldnames = [
        "num_validation_errors",
        "time_on_screen_seconds",
        "num_back_navigations",
        "nudging_level_profile",
        "screen_type",
        "steps_total",
        "current_step",
        "has_abandoned_before",
        "needs_help",
    ]

    nudging_levels = ["low", "medium", "high"]
    screen_types = ["balance", "onboarding", "send-money", "transactions"]

    rows = []
    for _ in range(n_rows):
        screen_type = random.choice(screen_types)
        nudging_level = random.choice(nudging_levels)

        # Reglas suaves para que el patrón tenga sentido
        if screen_type in ["balance"]:
            steps_total = 1
        elif screen_type in ["transactions"]:
            steps_total = 2
        else:
            steps_total = random.choice([3, 4])

        current_step = random.randint(1, steps_total)

        # Errores y navegación atrás
        num_validation_errors = random.choices(
            [0, 1, 2, 3],
            weights=[0.4, 0.3, 0.2, 0.1],
        )[0]

        num_back_navigations = random.choices(
            [0, 1, 2],
            weights=[0.7, 0.2, 0.1],
        )[0]

        # Tiempo en pantalla según dificultad
        base_time = random.randint(10, 30)
        extra_time_errors = num_validation_errors * random.randint(10, 20)
        extra_time_back = num_back_navigations * random.randint(5, 15)
        time_on_screen_seconds = base_time + extra_time_errors + extra_time_back

        has_abandoned_before = random.random() < 0.15

        # Etiqueta needs_help (regla + un poco de ruido)
        score = (
            num_validation_errors * 1.5
            + num_back_navigations * 1.0
            + (time_on_screen_seconds / 60.0)
            + (2 if has_abandoned_before else 0)
            + (1 if nudging_level == "high" else 0)
        )

        needs_help = 1 if score > 4.0 else 0

        # Introducir un poco de ruido (5%)
        if random.random() < 0.05:
            needs_help = 1 - needs_help

        rows.append({
            "num_validation_errors": num_validation_errors,
            "time_on_screen_seconds": time_on_screen_seconds,
            "num_back_navigations": num_back_navigations,
            "nudging_level_profile": nudging_level,
            "screen_type": screen_type,
            "steps_total": steps_total,
            "current_step": current_step,
            "has_abandoned_before": str(has_abandoned_before).lower(),
            "needs_help": needs_help,
        })

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def generate_accessibility_profile_data(
    n_rows=300, filename="accessibility_profile_training.csv"
):
    """
    Datos sintéticos para recomendación de perfil de accesibilidad.
    """
    fieldnames = [
        "can_read_small_text",
        "uses_screen_reader",
        "feels_confident_with_apps",
        "age_range",
        "avg_time_per_screen_seconds",
        "total_validation_errors",
        "requested_help_count",
        "theme",
        "screen_reader_mode",
        "font_scale",
        "nudging_level",
        "voice_feedback",
    ]

    confidence_levels = ["low", "medium", "high"]
    age_ranges = ["18_30", "31_50", "51_60", "60_plus"]

    rows = []
    for _ in range(n_rows):
        age_range = random.choices(
            age_ranges,
            weights=[0.25, 0.35, 0.2, 0.2],
        )[0]

        feels_confident = random.choices(
            confidence_levels,
            weights=[0.3, 0.4, 0.3],
        )[0]

        # Probabilidad de leer texto pequeño según edad
        if age_range in ["51_60", "60_plus"]:
            can_read_small_text = random.random() < 0.3
        else:
            can_read_small_text = random.random() < 0.8

        # Uso de lector de pantalla
        uses_screen_reader = random.random() < 0.2
        if age_range == "60_plus":
            uses_screen_reader = random.random() < 0.35

        # Métricas de uso
        base_time = random.randint(15, 35)
        extra_time_age = 10 if age_range in ["51_60", "60_plus"] else 0
        avg_time_per_screen = base_time + extra_time_age

        total_validation_errors = random.choices(
            [0, 1, 2, 3],
            weights=[0.3, 0.35, 0.25, 0.1],
        )[0]

        requested_help_count = random.choices(
            [0, 1, 2, 3],
            weights=[0.5, 0.3, 0.15, 0.05],
        )[0]

        # Lógica para outputs
        # Tema base
        if not can_read_small_text or age_range in ["51_60", "60_plus"]:
            theme = "large-text-high-contrast"
        else:
            theme = "standard-accessible"

        if uses_screen_reader:
            theme = random.choice(["large-text-high-contrast", "voice-assisted"])

        # font_scale
        if theme == "standard-accessible":
            font_scale = random.uniform(1.1, 1.3)
        else:
            font_scale = random.uniform(1.4, 1.8)

        # nudging_level
        if feels_confident == "low" or requested_help_count >= 2:
            nudging_level = "high"
        elif feels_confident == "medium":
            nudging_level = "medium"
        else:
            nudging_level = random.choice(["low", "medium"])

        # screen_reader_mode y voice_feedback
        screen_reader_mode = uses_screen_reader
        voice_feedback = uses_screen_reader or (nudging_level == "high")

        rows.append({
            "can_read_small_text": str(can_read_small_text).lower(),
            "uses_screen_reader": str(uses_screen_reader).lower(),
            "feels_confident_with_apps": feels_confident,
            "age_range": age_range,
            "avg_time_per_screen_seconds": avg_time_per_screen,
            "total_validation_errors": total_validation_errors,
            "requested_help_count": requested_help_count,
            "theme": theme,
            "screen_reader_mode": str(screen_reader_mode).lower(),
            "font_scale": round(font_scale, 2),
            "nudging_level": nudging_level,
            "voice_feedback": str(voice_feedback).lower(),
        })

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def generate_risk_data(n_rows=300, filename="risk_training.csv"):
    """
    Datos sintéticos para riesgo / fraude transaccional.
    """
    fieldnames = [
        "amount",
        "is_new_beneficiary",
        "hour_of_day",
        "num_past_transactions",
        "avg_transaction_amount",
        "max_transaction_amount",
        "num_transactions_to_beneficiary",
        "is_new_device",
        "geolocation_changed",
        "risk_level",
    ]

    rows = []
    for _ in range(n_rows):
        num_past_transactions = random.randint(1, 40)
        avg_transaction_amount = random.uniform(200.0, 1500.0)
        max_transaction_amount = avg_transaction_amount * random.uniform(1.2, 2.5)

        # Monto actual
        amount_factor = random.uniform(0.3, 4.0)
        amount = avg_transaction_amount * amount_factor

        is_new_beneficiary = random.random() < 0.35
        num_transactions_to_beneficiary = (
            0 if is_new_beneficiary else random.randint(1, 10)
        )

        hour_of_day = random.randint(0, 23)
        is_new_device = random.random() < 0.1
        geolocation_changed = random.random() < 0.1

        # Calcular un score de riesgo artificial
        score = 0.0

        # Monto vs promedio
        if amount_factor > 2.5:
            score += 2.0
        elif amount_factor > 1.5:
            score += 1.0

        # Beneficiario
        if is_new_beneficiary:
            score += 1.5
        elif num_transactions_to_beneficiary <= 1:
            score += 0.5

        # Horas “raras”
        if hour_of_day < 6 or hour_of_day > 22:
            score += 1.0

        # Dispositivo / ubicación
        if is_new_device:
            score += 1.0
        if geolocation_changed:
            score += 1.0

        # Historial bajo
        if num_past_transactions < 3:
            score += 0.5

        # Mapear score → risk_level
        if score <= 1.5:
            risk_level = "low"
        elif score <= 3.0:
            risk_level = "medium"
        else:
            risk_level = "high"

        # Introducir algo de ruido (poca cantidad)
        if random.random() < 0.05:
            if risk_level == "low":
                risk_level = "medium"
            elif risk_level == "medium":
                risk_level = random.choice(["low", "high"])
            else:
                risk_level = "medium"

        rows.append({
            "amount": round(amount, 2),
            "is_new_beneficiary": str(is_new_beneficiary).lower(),
            "hour_of_day": hour_of_day,
            "num_past_transactions": num_past_transactions,
            "avg_transaction_amount": round(avg_transaction_amount, 2),
            "max_transaction_amount": round(max_transaction_amount, 2),
            "num_transactions_to_beneficiary": num_transactions_to_beneficiary,
            "is_new_device": str(is_new_device).lower(),
            "geolocation_changed": str(geolocation_changed).lower(),
            "risk_level": risk_level,
        })

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


if __name__ == "__main__":
    print(f"[{datetime.now()}] Generando datos sintéticos...")

    generate_nudging_data(10000000)
    print(" - nudging_training.csv generado")

    generate_accessibility_profile_data(10000000)
    print(" - accessibility_profile_training.csv generado")

    generate_risk_data(10000000)
    print(" - risk_training.csv generado")

    print(f"[{datetime.now()}] Listo.")