FROM python:3.7.5

# Updating repository sources
RUN apt-get update

COPY requirements.txt /tmp/
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt

# Installing requirements
RUN apt-get install cron -yqq \
    curl

# Setting Working Directory
WORKDIR /home

CMD python scripts/stream_miner.py