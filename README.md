# API клиент для доступа к некоторым endpoint ресурса teachbase  

![Главная страница сайта](./static/img/firstpage.png)

Реализованы функции:

- Авторизация
- Проверка токена
- Отправка запросов

## Функционал

Ознакомиться с enpoints ресурса teachbase можно по адресу:
https://go.teachbase.ru/api-docs/index.html

В настоящем проекте реализовваны доступы:

- создание локального пользователя, личный кабинет с возможностью регистрации на teachbase

![Главная страница сайта](static\img\profile.png)

- вывод списка курсов

![Главная страница сайта](static\img\courses.png)

- детальное представление курса

![Главная страница сайта](static\img\coursedetail.png)

- запись зарегистрированного пользователя на сессию

## Установка

1. Клонируйте репозиторий на компьютер:
    >git clone git@github.com:Alexander-Fedorovtsev/teachbase_apiclient.git

2. Создайте и активируйте виртуальное окружение:
    >python -m venv venv
    >source venv/Scripts/activate

3. Установите зависимости:
    >pip install -r requirements.txt

4. Выполните миграции:
    >python manage.py makemigrations
    >python manage.py migrate

5. Запустите сервер локально:
    >python manage.py runserver

перейдите по адресу http://127.0.0.1:8000/

