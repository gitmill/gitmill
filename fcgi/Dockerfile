FROM dockerfile/ubuntu

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git fcgiwrap multiwatch && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --system --shell /bin/sh --group --disabled-password --home /home/git --uid 888 git

CMD HOME="/home/git" spawn-fcgi -u git -g git -p 8000 -n -- /usr/bin/multiwatch -f 4 /usr/sbin/fcgiwrap

VOLUME ["/data"]
EXPOSE 8000
