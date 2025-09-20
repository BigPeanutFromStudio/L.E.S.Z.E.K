# Jak skonfigurować dockera (prod)
0. Zainstaluj dockera https://www.docker.com/
1. Utwórz na wzór [.env_template](/.env_template) plik .env w root
   Koniecznie zmień:
   - DJANGO_SECRET_KEY
   - wszystkie zmienne środowiskowe dotyczące danych logowania
   - NIE ZAPOMNIJ DODAĆ IP SERWERA (IP W SIECI LOKALNEJ) DO `DJANGO_ALLOWED_HOSTS`
2. Odpal run.bat
3. Gotowe

> ⚠️ UWAGA run.bat należy udpalić tylko przy pierwszym uruchomieniu każde następne powinno się odbywać z docker desktop lub przez komendę `docker compose up` ⚠️