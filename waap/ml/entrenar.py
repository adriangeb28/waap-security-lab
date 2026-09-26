from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "logs" / "features_normal.csv"
MODEL = ROOT / "waap" / "ml" / "anomaly_bundle.pkl"

X = pd.read_csv(DATA)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)
model = IsolationForest(n_estimators=200, contamination="auto", random_state=42)
model.fit(Xs)

MODEL.parent.mkdir(parents=True, exist_ok=True)
joblib.dump({"scaler": scaler, "model": model, "features": list(X.columns)}, MODEL)
print(f"Modelo guardado en {MODEL}")
