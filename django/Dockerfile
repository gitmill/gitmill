FROM dockerfile/python

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y libpq-dev gettext && \
    rm -rf /var/lib/apt/lists/* && \
    pip install django gunicorn psycopg2 django-redis-sessions gitpython

RUN adduser --system --shell /bin/sh --group --disabled-password --home /home/git --uid 888 git

ADD . /django

WORKDIR /django
CMD python manage.py compilemessages && \
    python manage.py collectstatic --noinput && \
    python manage.py syncdb --noinput && \
    gunicorn --config gitmill/gunicorn.py gitmill.wsgi

VOLUME ["/data"]
EXPOSE 8000
