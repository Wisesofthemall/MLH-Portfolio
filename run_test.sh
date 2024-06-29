#!/bin/bash

# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

dnf install lsof && echo "Installed lsof package"

# Function to kill Flask process on port 5000 if it exists
kill_flask_process() {
    if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
        echo "Flask process found on port 5001. Killing it..."
        kill -9 $(lsof -ti :5001)
    fi
}

# Attempt to kill existing Flask process before starting a new one
kill_flask_process

# Function to start Flask server
start_flask_server() {
    flask run --host=0.0.0.0 --port=5001 &
    flask_pid=$!
    sleep 5 # Wait for Flask to start
}

# Retry logic to start Flask server
max_retries=1
retry_count=0
flask_started=false

while [ $retry_count -lt $max_retries ]; do
    start_flask_server
    sleep 5  # Wait for Flask to start
    if ps -p $flask_pid > /dev/null; then
        echo "Started Testing Flask server"
        flask_started=true
        break
    else
        retry_count=$((retry_count + 1))
    fi
done

# Check if Flask started successfully
if ! $flask_started; then
    echo "Failed CI Pipline. could not start Testing Flask server."

    exit 1
else
    echo "Site passed CI Pipline!"
    kill_flask_process # Ensure any lingering Flask process is killed
    exit 0
fi