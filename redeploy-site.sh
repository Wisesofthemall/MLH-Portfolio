#!/bin/bash

# Define the tmux session name
SESSION_NAME="flask_app"

# Function to check if the tmux session exists
session_exists() {
  tmux has-session -t $SESSION_NAME 2>/dev/null
}

# Close the existing tmux session if it exists
if session_exists; then
  echo "Closing existing tmux session..."
  tmux kill-session -t $SESSION_NAME
fi

# Pull updates from GitHub
echo "Pulling updates from GitHub..."
git pull origin main

# Start the Flask application in a new tmux session
echo "Starting Flask application in a new tmux session..."
tmux new-session -d -s $SESSION_NAME
tmux send-keys -t $SESSION_NAME 'source venv/bin/activate' C-m  # Adjust if using a different virtual environment setup
tmux send-keys -t $SESSION_NAME 'export FLASK_APP=app.py' C-m  # Adjust to your Flask entry point
tmux send-keys -t $SESSION_NAME 'flask run' C-m

echo "Flask application has been restarted in a new tmux session."
