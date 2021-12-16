# Note, this is only used by Dokku, Heroku would use the commands configured in heroku.yml
web: gunicorn openbook.wsgi -b :$PORT
scheduler: /usr/bin/supervisord -c /src/h2pro3/.docker/scheduler/supervisord.conf
worker: /usr/bin/supervisord -c /src/h2pro3/.docker/worker/supervisord.conf
