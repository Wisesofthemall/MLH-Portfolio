#!/bin/bash

# Get the current tmux session name
CURRENT_SESSION=$(tmux display-message -p '#S')

# Set OLD_SESSION to the current session name
OLD_SESSION="$CURRENT_SESSION"

# Increment NEW_SESSION based on the current session name
if [[ "$CURRENT_SESSION" =~ ([0-9]+)$ ]]; then
    VERSION=$((${BASH_REMATCH[1]} + 1))
    NEW_SESSION="${CURRENT_SESSION%.[0-9]*}.$VERSION"
else
    NEW_SESSION="$CURRENT_SESSION.1"
fi

# Create a new tmux session
tmux new-session -d -s "$NEW_SESSION"

# Change directory and update codebase within the new session
tmux send-keys -t "$NEW_SESSION" 'cd ~/MLH-Portfolio' Enter
tmux send-keys -t "$NEW_SESSION" 'echo "Changed directory to ~/MLH-Portfolio"' Enter

tmux send-keys -t "$NEW_SESSION" 'git fetch && git reset origin/main --hard' Enter
tmux send-keys -t "$NEW_SESSION" 'echo "Pulled latest changes from GitHub"' Enter

# Activate virtual environment and install dependencies
tmux send-keys -t "$NEW_SESSION" 'source python3-virtualenv/bin/activate' Enter
tmux send-keys -t "$NEW_SESSION" 'echo "Activated Python virtual environment"' Enter

tmux send-keys -t "$NEW_SESSION" 'pip install -r requirements.txt' Enter
tmux send-keys -t "$NEW_SESSION" 'echo "Installed latest dependencies"' Enter

# Start Flask server within the new session
tmux send-keys -t "$NEW_SESSION" 'flask run --host=0.0.0.0 &' Enter
tmux send-keys -t "$NEW_SESSION" 'echo "Started Flask server"' Enter

# Wait briefly for Flask to start (adjust sleep time as needed)
sleep 5

# Check if the old session exists and delete it
if tmux has-session -t "$OLD_SESSION" 2>/dev/null; then
    tmux kill-session -t "$OLD_SESSION"
    echo "Deleted old tmux session: $OLD_SESSION"
fi

echo "Site redeployed successfully!"
