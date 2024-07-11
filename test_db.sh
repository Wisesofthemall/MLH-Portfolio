#!/bin/bash

curl http://127.0.0.1:5000/api/timeline

ID=$(curl -X POST http://127.0.0.1:5000/api/timeline -d 'name=Lovinson&email=lovinson@gmail.com&content=Just Tested API for my portfolio site!' | jq -r '.id')


echo "ID: $ID"
echo "{\"id\":\"$ID\"}"
curl -s -X DELETE http://127.0.0.1:5000/api/timeline?id=$ID