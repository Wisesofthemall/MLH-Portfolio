#!/bin/bash

# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

