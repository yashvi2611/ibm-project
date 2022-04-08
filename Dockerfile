#FROM python:3.8-slim-buster
FROM ubuntu
WORKDIR /app-sgn
RUN apt-get update
RUN apt-get install -y python3 python3-pip iptables sqlite sqlite3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USER=root
COPY . .
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
CMD [ "python3" , "manage.py" , "runserver" , "0.0.0.0:8080" ]
