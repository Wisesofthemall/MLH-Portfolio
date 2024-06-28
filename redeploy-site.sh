#!/bin/sh

tmux kill-server

cd ~/MLH-Portfolio
echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard
echo "Pulled latest changes from GitHub"

source python3-virtualenv/bin/activate
echo "Activated Python virtual environment"

pip install -r requirements.txt
echo "Installed latest dependencies"

tmux new-session -d -s flask_server "cd ~/MLH-Portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
echo "Started Flask server"

echo "Site redeployed successfully!"