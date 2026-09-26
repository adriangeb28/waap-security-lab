from flask import Flask, request, jsonify
from rasp.guard import protect_query

app = Flask(__name__)

@protect_query
def make_login_query(username: str):
    return f"SELECT * FROM users WHERE username = '{username}'"

@app.get("/")
def index():
    return jsonify({"service": "RASP academic demo", "status": "ok"})

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/login")
def login():
    username = request.args.get("username", "")
    try:
        return jsonify({"query": make_login_query(username)})
    except PermissionError as exc:
        return jsonify({"blocked": True, "reason": str(exc)}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
