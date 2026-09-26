# WAAP Security Lab — IA, ML, RASP y DevSecOps

Laboratorio académico independiente para estudiar protección de aplicaciones web mediante WAAP/WAF, detección de anomalías con ML, RASP y controles DevSecOps.

## Arquitectura
- **Target:** OWASP Juice Shop en Docker.
- **WAAP:** ModSecurity + OWASP CRS como reverse proxy.
- **ML:** extracción de características y Isolation Forest.
- **RASP:** demostración académica de protección de una operación de consulta.
- **DevSecOps:** GitHub Actions con Semgrep, pip-audit, Trivy y Checkov.

## Puesta en marcha
1. Copiar `.env.example` a `.env`.
2. Ejecutar `docker compose up -d`.
3. Abrir el target en `http://localhost:3000`.
4. Acceder al proxy WAAP en `http://localhost:8080`.

## ML
```bash
cd waap/ml
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generar_trafico.py
python extraer_features.py
python entrenar.py
```

Los resultados experimentales deben generarse con tráfico real del laboratorio y guardarse en `evidencias/`; no se incluyen resultados inventados.

## RASP
La aplicación de demostración se encuentra en `app/` y la lógica de protección académica en `rasp/guard.py`.

## DevSecOps
El workflow está en `.github/workflows/seguridad.yml`. Los controles son demostrativos y deben ajustarse al entorno antes de un uso real.

## Evidencias
Las carpetas `evidencias/fase0` a `evidencias/fase7` sirven para registrar capturas, logs y resultados obtenidos durante la ejecución del laboratorio.
