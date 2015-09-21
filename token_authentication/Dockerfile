FROM ronald/tornado_base
RUN ["mkdir", "/var/www"]
RUN ["pip", "install", "hiredis", "redis", "tornado-redis"]
VOLUME /var/www
EXPOSE 80
