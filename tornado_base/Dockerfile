FROM debian:latest
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "python", "python-pip", "build-essential", "python-dev"]
RUN ["mkdir", "/root/.pip"]
ADD pip.conf /root/.pip/
RUN ["pip", "install", "tornado"]
