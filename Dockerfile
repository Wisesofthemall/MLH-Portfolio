FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y curl

RUN apt-get update && apt-get install -y jq



CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

