## Worker Service
- *Bug Fix:* Updated Redis connection to use REDIS_HOST environment variable instead of hardcoded 'localhost'.
- *Dockerfile:* Implemented a multi-stage build with a non-root user for improved security and smaller image size.
