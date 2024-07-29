FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

# Install dependencies and clean up
RUN apt-get update && \
    apt-get install -y \
        git \
        curl \
        jq \
        procps \
        lsof && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Command to run your Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

