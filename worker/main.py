import os
import redis
import time

# Configure connection
redis_host = os.getenv("REDIS_HOST", "redis")
client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

print(f"Worker started. Monitoring Redis at {redis_host}...")

# THIS LOOP KEEPS THE CONTAINER ALIVE
while True:
    try:
        # Just a simple heartbeat to prove it's working
        print("Worker is alive and waiting for tasks...")
        time.sleep(10) 
    except Exception as e:
        print(f"Error in loop: {e}")
        time.sleep(5)
