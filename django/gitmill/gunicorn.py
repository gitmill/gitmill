import multiprocessing

debug = True
daemon = False
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
user = 'git'
group = 'git'
forwarded_allow_ips = '*'
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
