#!/bin/bash

# Create Docker Compose file
cat <<EOF > docker-compose.yml
version: '3.8'
services:
  postgres:vv
    image: postgres:13
    environment:
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - "5432:5432"
  redash:
    image: redash/redash:latest
    environment:
      REDASH_DATABASE_URL: postgresql://${DB_USERNAME}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
    ports:
      - "5000:5000"
EOF

# Start Docker Compose
docker-compose up -d
