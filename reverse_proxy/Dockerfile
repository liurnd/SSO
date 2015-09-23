FROM nginx
RUN ["rm", "/etc/nginx/conf.d/default.conf"]
RUN ["mkdir", "-p", "/var/certs", "/var/pki/ca"]
ADD sso.conf /etc/nginx/conf.d/
ADD certs/verify_server/verify.crt /var/certs/
ADD certs/verify_server/verify.key /var/certs/
ADD certs/ca/cacert.pem /var/pki/ca/
EXPOSE 443
