FROM ubuntu:latest
MAINTAINER sheik kalidh "sheik.kalidh@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./requirements.txt /requirements.txt
COPY ./app /app
RUN pip install -r requirements.txt
WORKDIR /app
RUN pwd
RUN ls 
ENTRYPOINT ["python", "Changemanager.py"]
