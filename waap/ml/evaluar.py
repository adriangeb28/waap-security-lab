from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / "waap" / "ml" / "anomaly_bundle.pkl"
DATA = ROOT / "logs" / "evaluation_features.csv"
OUT = ROOT / "evidencias" / "fase3" / "evaluacion_ml.csv"

bundle = joblib.load(MODEL)
X = pd.read_csv(DATA)[bundle["features"]]
Xs = bundle["scaler"].transform(X)
model = bundle["model"]

result = X.copy()
result["anomaly_score"] = model.decision_function(Xs)
result["prediction"] = model.predict(Xs)
OUT.parent.mkdir(parents=True, exist_ok=True)
result.to_csv(OUT, index=False)
print(f"Evaluación escrita en {OUT}")
