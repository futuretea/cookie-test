FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY sources.list /etc/apt/sources.list
RUN apt update -y
RUN apt install -y vim net-tools
COPY main.py /app
