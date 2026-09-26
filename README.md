# 🛡️ WAAP Defense Lab 2026

Prototipo académico de una plataforma **WAAP** (reglas + IA/ML + RASP) con pipeline **DevSecOps**, desarrollado para el Taller No. 1 — Mecanismos de Seguridad Informática (Universidad Distrital FJDC).

## Arquitectura

Cliente → **Proxy WAAP** (ModSecurity + OWASP CRS) → **App Flask vulnerable + Agente RASP** → Logs/Métricas, con un **módulo IA/ML** (Isolation Forest) calculando un score de anomalía en paralelo, y un **pipeline CI/CD** validando código, dependencias e imagen antes de desplegar.

## Componentes

- `app/` — API Flask vulnerable + agente RASP (`rasp_agent.py`)
- `waap/rules/` — política del WAF como código
- `waap/ml/` — generación de tráfico, features, entrenamiento y scoring (Isolation Forest)
- `scripts/` — pruebas del RASP y generación de matrices de resultados
- `.github/workflows/` — pipeline DevSecOps (Semgrep, pip-audit, Trivy, Checkov)
- `results/` — evidencias por fase

## Arranque

```bash
cp .env.example .env
docker compose up -d --build
curl -i http://localhost:8080/health
```

## Flujo del laboratorio

```bash
python3 -m pip install -r waap/ml/requirements.txt
python3 waap/ml/make_normal_traffic.py
python3 waap/ml/features.py
python3 waap/ml/train.py
python3 waap/ml/evaluate.py
python3 scripts/run_lab.py
```

O con `make up`, `make ml`, `make test`, `make fixtures`.


## Informe técnico

Documentación completa de las 7 fases en `Informe_Tecnico_Taller_WAAP_2026.docx`.

## Aviso ético

Uso exclusivamente académico, contra el entorno aislado propio del laboratorio. No autorizado contra sistemas de terceros.
