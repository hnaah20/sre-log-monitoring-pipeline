FROM python:3.10-slim

WORKDIR /app

COPY web_log_sender.py .

RUN pip install requests

CMD ["python", "web_log_sender.py"]
