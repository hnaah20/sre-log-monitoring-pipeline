from flask import Flask, request, render_template_string, redirect, url_for, flash
import os

import os

# Ensure 'logs/' folder exists
if not os.path.exists('logs'):
    os.makedirs('logs')

log_path = os.path.join('logs', 'system.log')

from datetime import datetime

app = Flask(__name__)
app.secret_key = 'hannah-secure-token'  # Still needed for flashing UI messages

# ✅ NEW: Reusable tokens (per client)
valid_tokens = {
    "apple",
    "orange",
    "banana"
}

# Set up log directory
if not os.path.exists('logs'):
    os.makedirs('logs')

log_path = os.path.join('logs', 'system.log')

# HTML Upload Form (optional — for manual uploads)
HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Secure Log Upload (Token Auth)</title></head>
<body>
  <h2>Secure Log Upload Portal (Token Auth)</h2>
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <ul>
        {% for message in messages %}
          <li style="color:red;">{{ message }}</li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endwith %}
  <form method="post" enctype="multipart/form-data">
    <label>Enter Token:</label><br>
    <input type="text" name="token" required><br><br>
    <label>Paste Log Entry:</label><br>
    <textarea name="log_text" rows="5" cols="50"></textarea><br><br>
    <label>Or Upload Log File:</label><br>
    <input type="file" name="log_file"><br><br>
    <input type="submit" value="Upload Log">
  </form>
</body>
</html>
"""

# New route for automated clients (API)
@app.route('/send-log', methods=['POST'])
def receive_log():
    data = request.json
    token = data.get('token')
    windows_log = data.get('windows_log', '')
    metrics = data.get('system_metrics', {})

    if token not in valid_tokens:
        return {"status": "error", "message": "Invalid token"}, 401

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(log_path, 'a') as f:
        f.write(f"\n--- Log received at {timestamp} ---\n")
        f.write(f"[{token}] WINDOWS LOG:\n{windows_log.strip()}\n")
        f.write("SYSTEM METRICS:\n")
        for key, value in metrics.items():
            f.write(f"  {key}: {value}\n")
        f.write("--- End of log ---\n")

    return {"status": "success", "message": "Log + metrics received"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

