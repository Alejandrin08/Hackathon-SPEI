import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

os.makedirs("models", exist_ok=True)


def train_nudging_model():
    print("\nEntrenando modelo de NUDGING...")
    df = pd.read_csv("datasets/nudging_training.csv")

    X = df[
        [
            "num_validation_errors",
            "time_on_screen_seconds",
            "num_back_navigations",
            "steps_total",
            "current_step",
        ]
    ]
    y = df["needs_help"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy Nudging:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    joblib.dump(model, "models/nudging_model.pkl")
    print("✅ Modelo de Nudging guardado en models/nudging_model.pkl")


def train_accessibility_model():
    print("\nEntrenando modelo de PERFIL DE ACCESIBILIDAD...")
    df = pd.read_csv("datasets/accessibility_profile_training.csv")

    categorical_features = [
        "can_read_small_text",
        "uses_screen_reader",
        "feels_confident_with_apps",
        "age_range",
    ]

    # Convertir booleanos y texto a numéricos
    for col in categorical_features:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    X = df[
        [
            "can_read_small_text",
            "uses_screen_reader",
            "feels_confident_with_apps",
            "age_range",
            "avg_time_per_screen_seconds",
            "total_validation_errors",
            "requested_help_count",
        ]
    ]
    y = df["theme"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy Perfil Accesibilidad:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    joblib.dump(model, "models/accessibility_model.pkl")
    print("✅ Modelo de Accesibilidad guardado en models/accessibility_model.pkl")


def train_risk_model():
    print("\nEntrenando modelo de RIESGO / FRAUDE...")
    df = pd.read_csv("datasets/risk_training.csv")

    categorical_features = [
        "is_new_beneficiary",
        "is_new_device",
        "geolocation_changed",
    ]

    for col in categorical_features:
        df[col] = df[col].astype(str).map({"true": 1, "false": 0})

    X = df[
        [
            "amount",
            "is_new_beneficiary",
            "hour_of_day",
            "num_past_transactions",
            "avg_transaction_amount",
            "max_transaction_amount",
            "num_transactions_to_beneficiary",
            "is_new_device",
            "geolocation_changed",
        ]
    ]
    y = df["risk_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy Riesgo:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    joblib.dump(model, "models/risk_model.pkl")
    print("✅ Modelo de Riesgo guardado en models/risk_model.pkl")


if __name__ == "__main__":
    train_nudging_model()
    train_accessibility_model()
    train_risk_model()
    print("\n🎯 Todos los modelos entrenados y guardados correctamente.")