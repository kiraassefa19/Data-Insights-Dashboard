#!/bin/bash

# Variables
LOCAL_DASHBOARD_PATH="../../dashboard"
REMOTE_DASHBOARD_PATH="../../dashboard"

# Copy local dashboards to remote server
scp -r $LOCAL_DASHBOARD_PATH user@remote_host:$REMOTE_DASHBOARD_PATH
