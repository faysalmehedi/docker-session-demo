FROM alpine:latest

# Install python3 & pip
RUN apk add --update --no-cache
RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]
