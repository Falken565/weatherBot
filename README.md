# WeaherBot ULTIMATE PRO - тестовый проект
Веб интерфейс для рассылки погоды с помощью телеграм бота.
Чтобы получить рассылку надо:
- добавить бота в чат (предварительно создать его @BotFather)
- создать учетную запись на сайте
- зарегистрировать свой телеграм id
- отправлять погоду себе в телеграм (по условиям задания только погода в Москве)

### Как запустить проект:

Установить docker
```
# Установка утилиты для скачивания файлов
sudo apt install curl
# Эта команда скачает скрипт для установки докера
curl -fsSL https://get.docker.com -o get-docker.sh
# Эта команда запустит его
sh get-docker.sh
```

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Falken565/weatherBot.git
```

```
cd weatherbot
```

Cоздать файл с переменными окружения .env:

```
# блок базы данных
DB_ENGINE=django.db.backends.postgresql_psycopg2 # указываем бд, с которой работаем
POSTGRES_DB=weatherbot_db # имя бд 
POSTGRES_USER=falken # логин для подключения к бд (укажите свой)
POSTGRES_PASSWORD=123321 # пароль для подключения к бд (укажите свой)
DB_HOST=db # название контейнера
DB_PORT=5432 # порт для подключения к БД

# секретики для settings.py
SECRET_KEY=<super-secret-key>

# токены... 
TELEGRAM_TOKEN=<токен вашего бота>
KEY=<токен погодного сайта в данном случае: https://openweathermap.org/ >
```

Заглянуть в nginx и указать адрес сервера:

```
cd nginx
nano nginx.conf

server_name 127.0.0.1;
```

Запуск приложения в контейнерах:

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создаем пользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собираем статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```


### Где искать:
проект завускается на локальном сервере: 
```
http://127.0.0.1:8000/
```

### Информация о проекте:

- Проект работает с СУБД PostgreSQL.
- Проект запущен на локальном сервере в трёх контейнерах: nginx, PostgreSQL и Django+Gunicorn. 
- Данные сохраняются в volumes.
