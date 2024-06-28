#!/bin/sh

tmux attach-session -t $(tmux display-message -p '#S')

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