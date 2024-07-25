FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /apps
ENV PORT 8000

WORKDIR /apps

RUN apt update \
    && apt upgrade -y \
    && apt-get -y install gcc libmariadb-dev \
    && apt install -y default-mysql-client \
    && apt-get install -y default-libmysqlclient-dev \
    && apt install --no-install-recommends -y tzdata \
    && apt install -y graphviz \
    && apt-get install -y git \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /apps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE $PORT
