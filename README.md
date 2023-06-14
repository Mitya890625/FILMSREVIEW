# **Movie review application**



## Установка проекта

-git clone <https://github.com/Mitya890625/FILMSREVIEW.git>

## nastroit' virtual'noe okrujenie v papke s proektom
-poetry config virtualenvs.in-project true

## Установка виртуального окружения и зависимостей

-poetry install


## Активация вирутального окружения

-poetry shell

## Dobavit .env file v dir s settings.py 

Znacheniya peremennih okrujenia mojno posmotret' v .github/workflows/test_lint.yml

## Перейти в папку с manage.py

-cd moviereviews

## Primenit' migracii(sozdat DB)

-poetry run python manage.py migrate

## Запустить сервер

poetry run python manage.py runserver
