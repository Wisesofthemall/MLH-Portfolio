#!/bin/bash

start_time=$(date +%s)
# Commands to execute after attaching to tmux session
cd ~/MLH-Portfolio && echo "Changed directory to ~/MLH-Portfolio"

git fetch && git reset origin/main --hard && echo "Pulled latest changes from GitHub"

chmod +x python3-virtualenv/bin/activate && echo "Adding execute permissions to activate script"

source python3-virtualenv/bin/activate && echo "Activated Python virtual environment"

pip install -r requirements.txt && echo "Installed latest dependencies"

dnf install lsof && echo "Installed lsof package"

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
echo -e "\033[34mRunning Database tests\033[0m..."
chmod +x ./test_db.sh
./test_db.sh
DB_TEST_STATUS=$?
end_time=$(date +%s)
elapsed=$((end_time - start_time))
if [ $DB_TEST_STATUS -eq 0 ]; then
    echo -e "\033[32mDatabase CI passed\033[0m"

    exit 0
else
    echo -e "\033[31mDatabase CI failed\033[0m"

    exit 1
fi

exit 0


