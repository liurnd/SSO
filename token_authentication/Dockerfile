FROM ronald/tornado_base
RUN ["mkdir", "/var/www"]
RUN ["pip", "install", "hiredis", "redis", "tornado-redis"]
ADD www/startup.py /var/www/
CMD ["python", "/var/www/startup.py"]
EXPOSE 80
