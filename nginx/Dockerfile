FROM dockerfile/nginx

RUN adduser --system --shell /bin/sh --group --disabled-password --home /home/git --uid 888 git

ADD nginx.conf /etc/nginx/nginx.conf

CMD nginx

VOLUME ["/data"]
EXPOSE 80
