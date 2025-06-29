# RUNBOOK: System Log Monitoring Pipeline

## Overview

This project simulates real-time system telemetry (CPU, memory, disk) and forwards structured logs via token-authenticated REST endpoints. The logs are collected by a Flask-based receiver and visualized using Splunk dashboards. The entire pipeline is containerized with Docker and can optionally be deployed on cloud infrastructure using Terraform.

---

## Prerequisites

* Docker & Docker Compose installed
* Python 3.10+ (for local runs without Docker)
* Splunk Enterprise or Splunk Cloud (configured for log ingestion)
* Git (for cloning the repo)

---

## Setup & Deployment

### 1. Clone the repo

```bash
git clone https://github.com/hnaah20/sre-log-monitoring-pipeline.git
cd sre-log-monitoring-pipeline
```

### 2. Start services with Docker Compose

```bash
docker-compose up --build
```

This will launch:

* **Sender container**: generates telemetry and sends logs
* **Receiver container**: Flask app receiving logs and writing them to files/Splunk

### 3. Access services

* Flask Receiver API: `http://localhost:5000`
* Splunk Dashboard: `http://localhost:8000` (if running locally)

---

## Configuration

* Environment variables (e.g., tokens, Splunk URL) are set in `.env` or `docker-compose.yml`.
* Modify sender/receiver configs as needed for your environment.

---

## Usage

* The sender collects system metrics and pushes structured JSON logs periodically.
* The receiver authenticates incoming requests and processes logs to Splunk and local files.
* Splunk dashboards display real-time CPU, memory, disk usage, and alerts.

---

## Troubleshooting

| Symptom                         | Possible Cause                    | Recommended Action                                          |
| ------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| Cannot reach Flask endpoint     | Flask service not running         | Check `docker-compose logs receiver` and restart containers |
| Logs missing in Splunk          | Splunk config or token incorrect  | Verify Splunk HEC token and URL                             |
| Docker container fails to start | Port conflict or missing env vars | Check docker-compose.yml and `.env`                         |

---

## Helpful Commands

```bash
# Start containers detached
docker-compose up -d

# Stop containers
docker-compose down

# View logs for receiver container
docker logs -f <receiver_container_name>

# Rebuild containers after code changes
docker-compose up --build
```

---

## Contacts

**Hannah Susan Cherian**
📧 [x.hannah999@gmail.com](mailto:x.hannah999@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/hannah-susan-cherian694317275)

---
