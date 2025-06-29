FROM python:3.10-slim

WORKDIR /app

COPY web_log_receiver.py .

RUN pip install flask

CMD ["python", "web_log_receiver.py"]
