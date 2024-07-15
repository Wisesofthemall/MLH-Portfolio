#!/bin/bash

# Function to perform GET request
test_get() {
    echo "Testing GET /timeline_post"
    response=$(curl -s -X GET http://127.0.0.1:5000/timeline_post)
    echo "Response: $response"
    echo
}

# Function to perform POST request
test_post() {
    echo "Testing POST /timeline_post"
    response=$(curl -s -X POST http://127.0.0.1:5000/timeline_post \
                   -d "name=John Doe" \
                   -d "email=john.doe@example.com" \
                   -d "content=This is a test post.")
    echo "Response: $response"
    echo
}

# Run the tests
test_get
test_post
test_get
