#!/bin/bash

# Restart the myportfolio service
sudo systemctl restart myportfolio

end_time=$(date +%s)
elapsed=$((end_time - start_time))

# Check the status of the myportfolio service
if systemctl is-active --quiet myportfolio; then
    echo -e "\033[32mSite redeployed successfully!\033[0m"
    echo -e "\033[38;5;208mCD Pipeline Execution time: $elapsed seconds\033[0m"
    exit 0
else
    echo -e "\033[31mError: Failed to restart myportfolio service.\033[0m"
    echo -e "\033[38;5;208mCD Pipeline Execution time: $elapsed seconds\033[0m"
    exit 1
fi