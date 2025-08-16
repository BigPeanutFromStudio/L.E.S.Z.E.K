# Jak skonfigurować dockera (prod)
0. Utwórz na wzór [.env_template](/.env_template) .env file w root
1. Po sklonowaniu repo w root projektu użyj
``` pwsh
docker compose up --build
```
2. Następnie użyj w nowym terminalu
```pwsh
docker compose run django-web python manage.py migrate
```
3. Na koniec uruchom komendę
```pwsh
docker compose -f compose.yml exec django-web python manage.py collectstatic --no-input --clear
```