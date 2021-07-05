release: pyton manage.py makemigrations --no-input
release: pyton manage.py migrate auth --no-input
release: pyton manage.py migrate --no-input

web: gunicorn DjangoDeployment.wsgi

