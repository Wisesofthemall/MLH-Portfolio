#!/bin/bash

start_time=$(date +%s)
kill_flask_process() {
    if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
        echo "Killing exisiting Production Flask server..."
        kill -9 $(lsof -ti :5000)
    fi
}

# Attempt to kill existing Flask process before starting a new one
kill_flask_process

# Function to start Flask server
start_flask_server() {
    flask run --host=0.0.0.0 &
    flask_pid=$!
    sleep 1 # Wait for Flask to start
}

# Retry logic to start Flask server
max_retries=3
retry_count=0
flask_started=false

while [ $retry_count -lt $max_retries ]; do
    start_flask_server
    sleep 1  # Wait for Flask to start
    if ps -p $flask_pid > /dev/null; then
        echo "Starting Production Flask server"
        flask_started=true
        break
    else
        echo "Failed to start Production Flask server. Retrying..."
        retry_count=$((retry_count + 1))
        kill_flask_process  # Ensure any lingering Flask process is killed
    fi
done

end_time=$(date +%s)
elapsed=$((end_time - start_time))
# Check if Flask started successfully
if ! $flask_started; then
    echo -e "\033[31mError: Maximum retries reached. Production Flask server failed to start.\033[0m"
    echo -e "\033[38;5;208mCD Pipeline Execution time: $elapsed seconds\033[0m"

else
   echo -e "\033[32mSite redeployed successfully!\033[0m"
   echo -e "\033[38;5;208mCD Pipeline Execution time: $elapsed seconds\033[0m"

fi