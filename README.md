gitmill
======

A simple git repository manager for on-premise hosting.

Requirements
------------

* docker https://www.docker.com/
* fig http://www.fig.sh/

Setup
-------

After installing docker and fig, the system can be brought up by doing the following:

* Clone this repository somewhere, e.g. `/opt/gitmill` and `cd /opt/gitmill`
* Create your `fig.yml` file from template: `cp fig.yml.example fig.yml`
  * Modify `fig.yml` if necessary, the most important thing is to change the data volume mount source.
* For first run, postgresql needs some time to initialize properly, so start it first: `fig start postgres`
* Bring up the rest of the containers: `fig up -d --no-recreate`
* Setup a superuser: `fig run --rm django sudo -u git python manage.py createsuperuser`

