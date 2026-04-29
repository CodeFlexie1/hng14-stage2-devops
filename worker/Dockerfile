# STAGE 1: Builder
FROM python:3.9-slim AS builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Runner
FROM python:3.9-slim

RUN useradd --create-home devopsuser

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY . .
RUN chown -R devopsuser:devopsuser /app

USER devopsuser

# FIX: Use Python to check if it can successfully talk to Redis
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD python -c "import os, redis; redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379).ping()" || exit 1

CMD ["python", "main.py"]
