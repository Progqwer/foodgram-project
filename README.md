## Проект Foodgram

ip сервера: http://84.201.177.135/


Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.


В документации описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа.


## Тeхнологии проуктa

- Django                        2.2.16
- Django-filter                 22.1
- Djangorestframework           3.12.4
- Djangorestframework-simplejwt 5.2.2
- PyJWT                         2.1.0

## Запуск проекта локлаьно

- Клонировать репозиторий:

```
https://github.com/Progqwer/foodgram-project-react.git
```

- Перейти в директорию infra
```
cd infrta
```
- Создать и запустить контейнеры Docker, выполнить команду
```
 docker compose up -d --build
```

- После успешной сборки выполнить миграции:
```
 docker compose exec backend python manage.py migrate
```

- Собрать статику:
```
 docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных:
```
docker-compose exec backend python manage.py csv_download --path data/
```

- Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Для остановки контейнеров Docker:
```
sudo docker compose down         # останорвить и удалить контейнеры
sudo docker compose stop         # останорвить контейнеры
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

```

### Шаблон наполнения .env (не включен в репозиторий) расположенный по пути infra/.env
```bash
POSTGRES_USER=foodgram_db
POSTGRES_PASSWORD=postgres
POSTGRES_DB=foodgram_db
DEBUG=False
DJANGO_ALLOWED_HOSTS=['*']
```

- Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```
scp docker-compose.yml nginx.conf username@IP:/home/username/   # username - имя пользователя на сервере
                                                                # IP - публичный IP сервера


 - Создать и запустить контейнеры Docker, выполнить команду на сервере
```
sudo docker compose up -d
```                          

- После успешной сборки выполнить миграции:
```
sudo docker compose exec backend python manage.py migrate
```

- Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных:
```
sudo docker-compose exec backend python manage.py csv_download --path data/
```
## Авторы:
- Цыганков Илья
 
[![Django-app workflow](https://github.com/Progqwer/foodgram-project-react/actions/workflows/foodgram-project-react-workflow.yml/badge.svg)](https://github.com/Progqwer/foodgram-project-react/actions/workflows/foodgram-project-react-workflow.yml)


