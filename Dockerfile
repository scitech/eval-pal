FROM python:3.6-stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
  firejail

# Node
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash \
  && apt-get install -y nodejs

# Elixir, Ruby
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
  && dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get update && apt-get install -y --no-install-recommends \
  esl-erlang elixir ruby

RUN mkdir /opt/evalpal

RUN pip install --upgrade pip && pip install gunicorn

WORKDIR /opt/evalpal

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD evalpal /opt/evalpal

WORKDIR /opt

ENTRYPOINT gunicorn evalpal:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker
