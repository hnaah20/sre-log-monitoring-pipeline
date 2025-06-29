# System Log Monitoring Pipeline

A containerized log monitoring system using Python, Flask, Docker, and Splunk. Designed to simulate real-time telemetry, forward structured logs, and visualize system health in dashboards. Built to demonstrate practical observability, alerting, and infrastructure automation for Site Reliability Engineering workflows.

## Stack Used

- Python 3.10
- Docker + Docker Compose
- Flask (log receiver)
- psutil + requests (sender)
- Splunk (log visualization and alerting)
- Terraform (in progress) for EC2 deployment

## Features

- Real-time system telemetry generation (CPU, memory, disk)
- Token-based authentication
- Dockerized sender and receiver containers
- Structured JSON logs written to file and Splunk
- Dashboards showing system metrics and alerts
- Optional cloud deployment using Terraform
  
## 🧪 Screenshots

### 🎯 System Dashboard (Splunk)
![CPU over Time](splunk_screenshots/cpu_usage.png)
![System Message Breakdown](splunk_screenshots/sys_msg.png)
![System Health Table](splunk_screenshots/sys_health.png)

### 🐳 Docker Containers Running
![Docker ps output](splunk_screenshots/docker_ps.png)
![Docker logs](splunk_screenshots/docker_logs.png)

### 📥 Search and Reporting (Splunk)
![Splunk Searching](docs/splunk_search.png)

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/hnaah20/sre-log-monitoring-pipeline
cd sre-log-monitoring-pipeline

### 2. Start with Docker Compose
docker-compose up --build

### 3. Access services
Flask Log Receiver: http://localhost:5000
Splunk: http://localhost:8000 (if configured locally)
Logs are saved to receiver/logs/system.log
.
├── sender/
│   └── Dockerfile
│   └── web_log_sender.py
├── receiver/
│   └── Dockerfile
│   └── web_log_receiver.py
├── logs/
│   └── system.log
├── docker-compose.yml
├── README.md
└── RUNBOOK.md

## Author

**Hannah Susan Cherian**  
Final-year B.Tech CSE (Cybersecurity) | VIT-AP University  
📧 x.hannah999@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/hannah-susan-cherian694317275)

