#!/bin/bash

start_time=$(date +%s)
# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

dnf install lsof && echo "Installed lsof package"

# Function to kill Flask process on port 5000 if it exists
kill_flask_process() {
    if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
        echo "Killing exisiting Testing Flask server..."
        kill -9 $(lsof -ti :5001)
    fi
}

# Attempt to kill existing Flask process before starting a new one
kill_flask_process

# Function to start Flask server
start_flask_server() {
    flask run --host=0.0.0.0 --port=5001 &
    flask_pid=$!
    sleep 1 # Wait for Flask to start
}

# Retry logic to start Flask server
max_retries=1
retry_count=0
flask_started=false

while [ $retry_count -lt $max_retries ]; do
    start_flask_server
    sleep 1 # Wait for Flask to start
    if ps -p $flask_pid > /dev/null; then
        echo "Started Testing Flask server"
        flask_started=true
        break
    else
        retry_count=$((retry_count + 1))
    fi
done

end_time=$(date +%s)
elapsed=$((end_time - start_time))
# Run static analysis
if pylint app/*.py; then
    echo -e "\033[32mStatic analysis passed\033[0m"
else
    echo -e "\033[31mStatic analysis failed\033[0m"
    exit 1
fi

# Run pytest and capture the exit status
pytest tests/unit
TEST_STATUS=$?
if [ $TEST_STATUS -eq 0 ]; then
    echo -e "\033[32mUnit tests passed\033[0m"
else
    echo -e "\033[31mUnit tests failed\033[0m"
    exit 1
fi

# Check if Flask started successfully
if ! $flask_started; then
    echo -e "\033[31mFailed CI Pipeline. Could not start Testing Flask server.\033[0m" # Red color
    echo -e "\033[38;5;208mCI Pipeline Execution time: $elapsed seconds\033[0m" # Orange color

    exit 1
else
    echo -e "\033[32mSite passed CI Pipeline!\033[0m"
    kill_flask_process # Ensure any lingering Flask process is killed
    echo -e "\033[38;5;208mCI Pipeline Execution time: $elapsed seconds\033[0m" # Orange color
    exit 0
fi