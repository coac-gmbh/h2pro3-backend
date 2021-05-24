web: gunicorn openbook.wsgi -b :$PORT
scheduler: /usr/bin/supervisord -c /src/.docker/scheduler/supervisord.conf
worker: /usr/bin/supervisord -c /src/.docker/worker/supervisord.conf
