#!/bin/bash

# Define environment variables
DB_USERNAME="postgres"
DB_PASSWORD="Root@123"
DB_NAME="insights"

# Set up Docker containers
docker-compose up -d

# Wait for the containers to start
sleep 10

# Create network if it doesn't exist
docker network inspect insights-network &>/dev/null || \
docker network create insights-network

# Create a volume for PostgreSQL data
docker volume inspect insights-postgres-data &>/dev/null || \
docker volume create insights-postgres-data

# Run PostgreSQL container
docker run -d \
    --name insights-postgres \
    --network insights-network \
    -p 5432:5432 \
    -e POSTGRES_USER="$DB_USERNAME" \
    -e POSTGRES_PASSWORD="$DB_PASSWORD" \
    -e POSTGRES_DB="$DB_NAME" \
    -v insights-postgres-data:/var/lib/postgresql/data \
    postgres:latest

# Wait for PostgreSQL container to start
sleep 10

# Load initial data into PostgreSQL
docker exec -i insights-postgres psql -U "$DB_USERNAME" "$DB_NAME" < init.sql

echo "Dashboard system setup completed successfully."
