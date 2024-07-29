#!/bin/bash

start_time=$(date +%s)

# Define the base URL for the API
base_url="https://mlh-lovinson.duckdns.org/api/timeline"

# Make a GET request to fetch timeline posts
curl_output=$(curl -s "$base_url")

# Check if the curl command succeeded
if [ $? -ne 0 ]; then
    echo -e "\033[31mFailed to fetch timeline posts.\033[0m"
    exit 1
fi

# Display the fetched timeline posts
echo "$curl_output"
echo

# Make a POST request to create a new timeline post
post_output=$(curl -s -X POST "$base_url" -d 'name=Lovinson&email=lovinson@gmail.com&content=Just Tested API for my portfolio site!')

# Check if the POST request succeeded and retrieve the ID
if [ $? -ne 0 ]; then
    echo -e "\033[31mError: Failed to create a new timeline post.\033[0m"
    exit 1
fi

# Extract the ID using jq
ID=$(echo "$post_output" | jq -r '.id')

# Make a DELETE request to delete the newly created post
delete_output=$(curl -s -X DELETE "$base_url?id=$ID")

# Check if the DELETE request succeeded
if [ $? -ne 0 ]; then
    echo -e "\033[31mError: Failed to delete the post with ID: $ID\033[0m"
    exit 1
fi

# Exit with success status
exit 0
