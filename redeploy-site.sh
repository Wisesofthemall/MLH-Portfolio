#!/bin/bash

# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
    echo "Flask process found on port 5000. Killing it..."
    kill -9 $(lsof -ti :5000)
fi

flask run --host=0.0.0.0 && echo "Started Flask server"

echo "Site redeployed successfully!"
