import random
import psutil
import datetime
import subprocess
import requests
import time
import os

# === CONFIGURATION ===
TOKEN = "apple"  # Replace with your valid token
SERVER_URL = "http://192.168.230.1:5000/send-log"  # Use your real IP if testing across devices
EXPORTED_LOG_PATH = r"C:\Users\Public\system_logs.txt"
LINES_TO_SEND = 10  # ✅ Only send last 10 lines now
SLEEP_INTERVAL = 10  # 10 seconds


# === STEP 1: Export Windows Event Logs ===
def export_windows_event_logs():
    powershell_command = (
    f'Get-WinEvent -LogName System -MaxEvents 100 | Out-File -FilePath "{EXPORTED_LOG_PATH}" -Encoding utf8'
)
    try:
        subprocess.run(["powershell", "-Command", powershell_command], check=True)
        print(f"✅ Exported logs to {EXPORTED_LOG_PATH}")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to export logs:", e)
        return False
    return True

# === STEP 2: Read Last N Lines ===
def read_log_lines(path, count):
    if not os.path.exists(path):
        return "ERROR: Exported log file not found."
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        return "".join(lines[-count:]) if lines else "Log file is empty."

# === STEP 3: Send to Flask Server ===
def send_log(log_text):
    # Collect system metrics again at send time
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    timestamp = datetime.datetime.now().isoformat()

    system_metrics = {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
        "timestamp": timestamp,
        "source": "system_monitor"
    }

    # Alert conditions
    if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
        system_metrics["alert"] = "High resource usage detected"

    # SOC simulated activity
    if random.random() < 0.3:
        system_metrics["message"] = "Failed login attempt from IP 192.168.1.101"
    else:
        system_metrics["message"] = "System operating normally"

    # Final payload
    payload = {
        "token": TOKEN,
        "windows_log": log_text,
        "system_metrics": system_metrics
    }

    try:
        response = requests.post(SERVER_URL, json=payload)
        result = response.json()
        print(f"[{time.ctime()}] ✅ Sent log | Status: {result['status']} | Message: {result['message']}")
    except Exception as e:
        print(f"[{time.ctime()}] ❌ Failed to send log:", e)


# === STEP 4: Auto-delete after Upload ===
def delete_log_file(path):
    try:
        os.remove(path)
        print(f"🧹 Deleted exported log file: {path}")
    except Exception as e:
        print(f"⚠️ Could not delete exported file: {e}")

# === MAIN LOOP ===
if __name__ == "__main__":
    print("📤 Starting hourly real log upload...")

    while True:
        print(f"[{time.ctime()}] 🛰️ Sending telemetry to server...")

        if export_windows_event_logs():
            logs = read_log_lines(EXPORTED_LOG_PATH, LINES_TO_SEND)
            send_log(logs)
            delete_log_file(EXPORTED_LOG_PATH)

        print(f"⏱️ Sleeping for {SLEEP_INTERVAL // 60} minutes...\n")
        time.sleep(SLEEP_INTERVAL)

