cd /code
python manage.py makemigrations polls
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 &

uvicorn mysite.asgi:fastapp --reload --port 8001 --host 0.0.0.0 &

wait -n 

exit $?
