from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "application": "ITSM Ticket API",
        "status": "running",
        "environment": os.getenv("APP_ENV", "development")
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/tickets")
def tickets():
    return jsonify([
        {"id": 101, "title": "VPN access issue", "status": "Open"},
        {"id": 102, "title": "Password reset", "status": "In Progress"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
