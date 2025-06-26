import os
import time

# Send 5 logs with 10-second gaps
for i in range(5):
    print(f"Sending log {i + 1}")
    os.system("python web_log_sender.py")
    time.sleep(10)  # Adjust delay here (in seconds)
