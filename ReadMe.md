# Welcome to L.E.S.Z.E.K (Losowy Egzaminator Szkolny Z Egzaminów Klasyfikacyjnych)

## TODO

- [ ] Aplikacje pytań powinny być usuwane jeśli aplikacja dotycząca tego samego pytania została zaakceptowana
- [ ] Odpowiedzi na pytanie nie zmieniaja się po przejściu do następnego -> brak znalezionej metody powtórzenia błędu

## Przygotowanie

Aby system działał należy zainstalować pythona w wersji przynajmniej 3.13.1 oraz bibliotekę *Django*.

Instalacja *Django*:
1. 
```pwsh
$ pip install Django
```

Systemu należy używać poprzez wirtualne środowisko pythona. Po sklonowaniu repozytorium należy jednorazowo stworzyć to środowisko.
Aby je stworzyć postępuj wedle następujących kroków.

1. Stwórz wirtualne środowisko (nazwę "leszek" można zastąpić dowolną nazwą)
```pwsh
$  py -m venv leszek
```

## Jak zacząć

Wszystkie akcje wykonuj używając wirtualnego środowiska pythona. Aby do niego wejść wykonaj poniższe kroki.

1. Jeśli używasz powershell użyj 
```pwsh
$ Set-ExecutionPolicy Unrestricted -Scope Process
```
2. Następnie uruchom skrypt "activate" znajdujący się w folderze L.E.S.Z.E.K
```pwsh
$ .\leszek\Scripts\activate
```

## Jak włączyć serwer

1. Przejdź do folderu leszek_projekt
```pwsh
$ cd .\leszek_projekt
```
2. Aby uruchomić serwer użyj komendy:
```pwsh
$ py manage.py runserver
```

## Jak zaimportować dane z systemu A.S.P.E.K.T

1. Do folderu "leszek_projekt\import_data" przenieś plik "questions_import.json" otrzymany po użyciu A.S.P.E.K.T
2. Użyj komendy:
```pwsh
$ py manage.py loaddata .\import_data\questions_export.json
```
3. Do folderu "leszek_projekt\static_files\media" przenieś wszystkie pliki otrzymane po użyciu A.S.P.E.K.T (powinny znajdować się w folderze "media") 