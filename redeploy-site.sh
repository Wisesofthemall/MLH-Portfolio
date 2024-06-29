#!/bin/bash

# Commands to execute after attaching to tmux session
# cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

# git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

# chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

# source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

# pip install -r requirements.txt && echo "Installed latest dependencies"

# dnf install lsof && echo "Installed lsof package"

# Function to kill Flask process on port 5000 if it exists
kill_flask_process() {
    if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
        echo "Flask process found on port 5000. Killing it..."
        kill -9 $(lsof -ti :5000)
    fi
}

# Attempt to kill existing Flask process before starting a new one
kill_flask_process

# Function to start Flask server
start_flask_server() {
    flask run --host=0.0.0.0 &
    flask_pid=$!
    sleep 5 # Wait for Flask to start
}

# Retry logic to start Flask server
max_retries=3
retry_count=0
flask_started=false

while [ $retry_count -lt $max_retries ]; do
    start_flask_server
    sleep 5  # Wait for Flask to start
    if ps -p $flask_pid > /dev/null; then
        echo "Started Flask server"
        flask_started=true
        break
    else
        echo "Failed to start Flask server. Retrying..."
        retry_count=$((retry_count + 1))
        kill_flask_process  # Ensure any lingering Flask process is killed
    fi
done

# Check if Flask started successfully
if ! $flask_started; then
    echo "Error: Maximum retries reached. Flask server failed to start."
else
    echo "Site redeployed successfully!"
fi