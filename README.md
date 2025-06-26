# SRE Log Monitoring Pipeline

A real-world simulation of a system log collection and monitoring pipeline for SRE and SOC roles. This project uses Python to collect system metrics and Windows logs in real time, transmits them securely via a Flask-based API, and forwards all telemetry into Splunk for dashboarding and alerting.

## 📌 Features

- Real-time telemetry every 10 seconds
- CPU, memory, disk usage, and event log extraction via PowerShell
- Token-authenticated log transmission to Flask server
- Splunk dashboard integration for visualization
- Alerting logic for high memory usage and failed login attempts
- Regex-based field extraction for CPU, memory, disk, alert, and message

## 🎯 Tech Stack

- Python + Flask
- psutil + subprocess + requests
- Splunk (dashboarding + alerting)
- PowerShell (log export)

## 📊 Live Visualizations

| Metric | Description |
|--------|-------------|
| 📈 `system_metrics_dashboard.png` | CPU, memory, and disk usage trends over time |
| 🔔 `high_memory_alert.png`       | Triggered alert when memory > 85%             |
| ❌ `failed_login_event.png`      | Detected suspicious activity in log stream    |
| 🛰️ `real_time_logs.png`          | 10-second log transmission simulation         |

## 🚀 Use Case

Designed to simulate real telemetry pipelines seen in SRE and SOC teams — ideal for incident response, root cause analysis, and performance monitoring.

## 📁 Folder Structure

sre-log-monitoring-pipeline/
├── log_sender.py
├── log_receiver.py
├── README.md
└── screenshots/
├── real_time_logs.png
├── system_metrics_dashboard.png
├── high_memory_alert.png
└── failed_login_event.png


## 🧠 Author

**Hannah Susan Cherian**  
DFIR Enthusiast | Building SRE & SOC Skills | Security+ Certified | VIT-AP University 

