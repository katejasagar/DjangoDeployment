release: python manage.py makemigrations --no-input
release: python manage.py migrate auth --no-input
release: python manage.py migrate --no-input

web: gunicorn DjangoDeployment.wsgi --log-file -

