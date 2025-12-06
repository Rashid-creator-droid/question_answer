

# question_answer
# Стек технологий
<div id="badges" align="center">
  <img src="https://img.shields.io/badge/Python%203.10-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/FastAPI%20-white?style=for-the-badge&logo=fastapi&"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
</div>

# Описание проекта
### Вопрос - ответ
Проект предоставляет функционал работы с вопросами и ответами.

### Регистрация и авторизация.
Пользователь имеет возможность зарегистрироваться в системе, пройти авторизацию и получить доступ к своему личному кабинету.
В личном кабинете доступно изменение персональных данных.

Авторизация реализована через куки (cookie-based authentication).
После успешного входа сервер устанавливает защищённую cookie с токеном, которая автоматически отправляется браузером при следующих запросах. Это позволяет пользователю оставаться авторизованным без необходимости вручную передавать токены.

### Логирование.
Реализована система логирование исключений. На уровне проекта в папке logs сохраняются файлы с логами.

### Версионирование.
В проекте реализовано версионирование API. На данный момент доступна версия v1.

# Установка проекта.
Перед установкой проекта необходимо в корне проекта создать файл .env с переменными окруженя. Пример:
```.dotenv
POSTGRES_DB=test_base
POSTGRES_DB_TEST=test
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET=xutyeq
``` 
## Установка и запуск проекта через Docker
### Склонировать репозиторий и перейти в папку с проектом в командной строке
```bash
    git clone https://github.com/Rashid-creator-droid/question_answer
```
```bash
    cd question_answer
```
### Запустить сборку контейнера Docker Compose V2
По умолчанию проект использует образ из Docker Hub. Для запуска:
```bash
    docker compose up -d
``` 
Если вы хотите использовать локальную сборку образа, можно заменить в docker-compose.yml строку с image на:
```yml
build: .
```
### Проект будет доступен по адресу
```
http://localhost:8000/
```

## Документация проекта openapi доступна по адресу 
```
http://localhost:8000/docs/v1
```


## Аутентификация
### Регистрация
- POST запрос с данными /api/auth/register
```json
{
  "email": "user@example.com",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false,
  "username": "string"
}
```
### Авторизация 
- POST form-запрос /api/auth/jwt/login
## Внимание!
- Особенности авторизации: для авторизации в поле username используется email указанный при регистрации

## Установка проекта из репозитория  GitHub.
### Установить Python 3.10
- Для Windows https://www.python.org/downloads/
- Для Linux 
```
sudo apt update
sudo apt -y install python3-pip
sudo apt install python3.10
``` 
### Клонировать репозиторий и перейти в него в командной строке.
```
 git clone https://github.com/Rashid-creator-droid/question_answer
``` 
###  Развернуть виртуальное окружение.
```
python -m venv venv
``` 
 - для Windows;
```
venv\Scripts\activate.bat
``` 
 - для Linux и MacOS.
``` 
source venv/bin/activate

```
### Установить систему контроля зависимостей Poetry
```
pip install poetry
``` 
### Установить зависимости
```
poetry install
```
### Команда для применения миграций
```
alembic upgrade head
```

### Запуск проекта
```
python main.py
```
### Проект будет доступен по адресу.
```
http://127.0.0.1:8001/
```
### Документация проекта
```
http://127.0.0.1:8001/docs/v1
```
