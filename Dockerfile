FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

