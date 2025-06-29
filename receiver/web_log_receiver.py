from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# === CONFIGURATION ===
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system.log")
VALID_TOKENS = {"apple", "orange", "banana"}

# Ensure logs/ directory exists
os.makedirs(LOG_DIR, exist_ok=True)

@app.route('/send-log', methods=['POST'])
def receive_log():
    data = request.get_json()

    if not data:
        return jsonify({"status": "fail", "message": "Missing JSON body"}), 400

    token = data.get("token")
    if token not in VALID_TOKENS:
        return jsonify({"status": "fail", "message": "Invalid token"}), 401

    # Add server-side timestamp if missing
    if "time" not in data:
        data["time"] = datetime.now().isoformat()

    # Append to log file as JSON
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")

    return jsonify({"status": "success", "message": "Log received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
