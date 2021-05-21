FROM python:3.7.3

RUN apt-get -y update && apt-get -y upgrade &&  apt-get install -y ffmpeg

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup workdir
RUN mkdir /src
WORKDIR /src

COPY . /src
