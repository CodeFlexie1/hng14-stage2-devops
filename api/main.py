from fastapi import FastAPI
from uuid import uuid4
import os
import redis

app = FastAPI()

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

@app.get("/")
def home():
    return {"status": "healthy"}

@app.post("/submit")
def submit_job():
    job_id = str(uuid4())
    # Pushes the ID to the Redis queue for the worker
    redis_client.lpush("job_queue", job_id)
    return {"status": "success", "job_id": job_id}

# Route to check status (your dashboard will need this)
@app.get("/status/{job_id}")
def get_status(job_id: str):
    # Check if the worker moved it to a 'completed' list or similar
    # For now, we'll just return that it's processing
    return {"job_id": job_id, "status": "processing"}
