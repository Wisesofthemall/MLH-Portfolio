#!/bin/bash

# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

# Function to kill Flask process on port 5000 if it exists
kill_flask_process() {
    if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
        echo "Flask process found on port 5000. Killing it..."
        kill -9 $(lsof -ti :5000)
    fi
}

# Attempt to kill existing Flask process before starting a new one
kill_flask_process

# Start Flask and capture its process ID
flask run --host=0.0.0.0 &
flask_pid=$!

# Wait for Flask to start (optional)
sleep 5  # Adjust this wait time as needed

# Check if Flask process is still running
if ps -p $flask_pid > /dev/null; then
    echo "Started Flask server"
else
    echo "Error: Flask server failed to start"
fi



echo "Site redeployed successfully!"
