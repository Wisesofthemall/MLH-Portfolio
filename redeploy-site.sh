#!/bin/sh

if ! tmux has-session -t mysession; then
    tmux new-session -d -s mysession
fi

# Attach to the tmux session
tmux attach-session -t mysession

cd ~/MLH-Portfolio
echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard
echo "Pulled latest changes from GitHub"

source python3-virtualenv/bin/activate
echo "Activated Python virtual environment"

pip install -r requirements.txt
echo "Installed latest dependencies"

flask run --host=0.0.0.0
echo "Started Flask server"

echo "Site redeployed successfully!"