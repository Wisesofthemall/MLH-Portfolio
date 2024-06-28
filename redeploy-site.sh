#!/bin/bash

SESSION_NAME="Flask server"

# Check if tmux session exists, otherwise create a new one
if ! tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    tmux new-session -d -s "$SESSION_NAME"
fi

# Attach to the tmux session
tmux attach-session -t "$SESSION_NAME"

# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

flask run --host=0.0.0.0 && echo "Started Flask server"

echo "Site redeployed successfully!"
