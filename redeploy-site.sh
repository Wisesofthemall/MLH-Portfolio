#!/bin/sh

tmux kill-server

cd ~/MLH-Portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux new-session -d -s flask_server "cd ~/MLH-Portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"

echo "Site redeployed successfully!"