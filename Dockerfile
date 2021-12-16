FROM python:3.7.3

RUN apt-get -y update && apt-get -y upgrade &&  apt-get install -y ffmpeg && apt-get install -y supervisor

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup workdir
RUN mkdir -p /src/h2pro3
WORKDIR /src/h2pro3

COPY . /src/h2pro3
