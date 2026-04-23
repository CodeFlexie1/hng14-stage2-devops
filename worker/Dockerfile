# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.11-slim
# Create the non-root user (HNG REQUIREMENT)
RUN useradd -m -u 1001 appuser
WORKDIR /app
COPY --from=builder /root/.local /home/appuser/.local
COPY . .
RUN chown -R appuser:appuser /app
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH

# Workers usually don't have a port to expose, but they need a healthcheck!
# We check if the process is running
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD ps aux | grep "python" || exit 1

CMD ["python", "main.py"]
