# API для Yatube

REST API социальной сети Yatube: публикации, комментарии, группы и подписки.
Поддерживается JWT-аутентификация, а изменять и удалять контент может только
его автор.

## Установка и запуск

```powershell
git clone <URL-репозитория>
cd api-final-yatube-ad
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Документация Redoc доступна по адресу
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/).

## Примеры запросов

Получить JWT-токен:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{"username": "user", "password": "password"}
```

Создать публикацию:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{"text": "Моя первая публикация"}
```

Подписаться на пользователя:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{"following": "another_user"}
```
