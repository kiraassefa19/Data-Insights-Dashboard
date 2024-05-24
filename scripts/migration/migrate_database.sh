#!/bin/bash

# Variables
LOCAL_DB_URL="postgresql://postgres:Root@123@localhost:5432/insights"
REMOTE_DB_URL="postgresql://remote_user:remote_password@remote_host:5432/remote_db"

# Dump the local database
pg_dump $LOCAL_DB_URL > local_dump.sql

# Restore the dump to the remote database
psql $REMOTE_DB_URL < local_dump.sql
