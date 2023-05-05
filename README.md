# praktikum_new_diplom
Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Список категорий может быть расширен.

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.


## Тeхнологии проуктa

- Django                        2.2.16
- Django-filter                 22.1
- Djangorestframework           3.12.4
- Djangorestframework-simplejwt 5.2.2
- PyJWT                         2.1.0

## Запуск проекта

- Создание виртуального окружения
```
python -m venv venv
```

- Активация виртуального окружения

- Установка зависимостей
```
pip install -r requirements.txt
```

- Перейти в директорию api_yamdb
```
cd api_yamdb
```
- Выполнить миграции
```
python manage.py makemigrations

python manage.py migrate
```

- Запуск локального сервера
```
python manage.py runserver
```




## Загрузка данных из csv

Перейти в директорию api_yamdb

```
cd api_yamdb
```

Запустить зазгрузку данных из csv

```
python manage.py csv_download
```

### Настройка проекта для развертывания на удаленном сервере

1. Установите на сервере `docker` и `docker-dompose`.
2. Локально отредактируйте файл `infra/nginx.conf`, в строке `server_name` впишите IP-адрес сервера.
3. Скопируйте файлы `docker-compose.yaml` и `nginx/defult.conf` из директории `infra` на свой сервер:

```bash
    scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yaml
    scp default.conf <username>@<host>:/home/<username>/nginx/default.conf
```

4. Добавьте в Secrets GitHub следующие переменные:

```bash
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=имя базы данных postgres
    DB_USER=пользователь бд
    DB_PASSWORD=пароль
    DB_HOST=db
    DB_PORT=5432

    DOCKER_PASSWORD=пароль от DockerHub
    DOCKER_USERNAME=имя пользователя

    SECRET_KEY=секретный ключ проекта django

    USER=username для подключения к серверу
    HOST=IP сервера
    PASSPHRASE=пароль для сервера, если он установлен
    SSH_KEY=ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa - копировать с текстом)

    TELEGRAM_TO=ID чата, в который придет сообщение
    TELEGRAM_TOKEN=токен вашего бота
```

### Шаблон наполнения .env (не включен в репозиторий) расположенный по пути infra/.env
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## Авторы:
- Книженцев Иван
- Цыганков Илья
- Тамерлан Салим

ip сервера: 84.201.178.33
 
[![Django-app workflow](https://github.com/Progqwer/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/Progqwer/yamdb_final/actions/workflows/yamdb_workflow.yml)

