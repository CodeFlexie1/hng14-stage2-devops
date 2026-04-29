# STAGE 1: Builder
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# STAGE 2: Runner (Production)
FROM node:18-alpine

WORKDIR /app

# Copy everything from the builder stage
COPY --from=builder /app /app

# Give ownership of the files to the non-root 'node' user
RUN chown -R node:node /app

# Switch to the non-root user
USER node

# Expose the port
EXPOSE 3000

# HEALTHCHECK required by the task
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD wget -qO- http://localhost:3000/ || exit 1

# Start the application
CMD ["npm", "start"]
