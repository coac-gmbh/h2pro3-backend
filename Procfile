# Note, this is only used by Dokku, Heroku would use the commands configured in heroku.yml
web: gunicorn openbook.wsgi -b :$PORT
scheduler: /usr/bin/supervisord -c /opt/okuna-api/.docker/scheduler/supervisord.conf
worker: /usr/bin/supervisord -c /opt/okuna-api/.docker/worker/supervisord.conf
