FROM python:3
WORKDIR /aloha-way
VOLUME create pgdata
COPY requirements.txt /aloha-way/
RUN pip install -r requirements.txt
COPY . /aloha-way/