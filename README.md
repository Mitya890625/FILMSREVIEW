# **Movie review application**



## Установка проекта


### Скачать проект с гитхаба
-git clone <https://github.com/Mitya890625/FILMSREVIEW.git>

### Настроить виртуальное окружение в папке с проектом
-poetry config virtualenvs.in-project true

### Установка виртуального окружения и зависимостей

-poetry install


### Активация вирутального окружения

-poetry shell

### Добавить .env файл в директорию с settings.py 

Требуемые переменные окружения и их значения:
DATABASE_URL=sqlite://./db.sqlite3
MODE_DEBUG=1
SECRET_KEY=1

### Перейти в директорию с manage.py

### Создать базу данных и заполнить таблицами

-poetry run python manage.py migrate

### Запустить сервер

poetry run python manage.py runserver
