import random
import datetime
import requests
import time

# === CONFIGURATION ===
TOKEN = "apple"  # Must match one from receiver
SERVER_URL = "http://receiver:5000/send-log"  # Docker internal hostname
SLEEP_INTERVAL = 10  # Send every 10 seconds

# === LOG SIMULATOR ===
def send_log():
    cpu = round(random.uniform(15, 85), 2)
    memory = round(random.uniform(30, 90), 2)
    disk = round(random.uniform(20, 80), 2)
    timestamp = datetime.datetime.now().isoformat()

    alert = None
    if cpu > 75:
        alert = "⚠️ High CPU usage"
    elif memory > 70:
        alert = "⚠️ High memory usage"
    elif disk > 65:
        alert = "⚠️ Low disk space"

    message = "System operating normally"
    if random.random() < 0.2:
        message = "⚠️ Suspicious network scan from 172.18.0.8"

    payload = {
        "token": TOKEN,
        "windows_log": "Simulated log entry: container running",
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "time": timestamp,
        "message": message,
        "alert": alert,
        "source": "container_sentinel"
    }

    try:
        response = requests.post(SERVER_URL, json=payload)
        print(f"[{time.ctime()}] ✅ Log sent | {response.status_code}")
    except Exception as e:
        print(f"[{time.ctime()}] ❌ Failed to send log: {e}")

# === LOOP ===
if __name__ == "__main__":
    print("📤 Starting SRE log sender...")
    while True:
        send_log()
        time.sleep(SLEEP_INTERVAL)
