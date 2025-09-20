@echo off

docker compose up --build -d


timeout /t 1


docker compose -f compose.yml exec django-web python manage.py migrate 
docker compose -f compose.yml exec django-web python manage.py loaddata ./import_data/codes.json 
docker compose -f compose.yml exec django-web python manage.py createsuperuser --noinput
docker compose -f compose.yml exec django-web python manage.py collectstatic --no-input --clear