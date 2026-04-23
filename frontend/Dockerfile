# Use your existing base image (e.g., node:18-slim or node:20)
FROM node:18-slim

# Install curl (This is the missing step!)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Your existing build steps below...
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
