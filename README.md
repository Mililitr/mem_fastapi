# Meme API

## Описание

Веб-приложение на Python с использованием FastAPI, которое предоставляет API для работы с коллекцией мемов.

## Функциональность

- **GET /memes:** Получить список всех мемов (с пагинацией).
- **GET /memes/{id}:** Получить конкретный мем по его ID.
- **POST /memes:** Добавить новый мем (с картинкой и текстом).
- **PUT /memes/{id}:** Обновить существующий мем.
- **DELETE /memes/{id}:** Удалить мем.

## Запуск проекта

1. Клонируйте репозиторий.
2. Создайте файл `.env` и добавьте в него конфигурацию S3.
3. Запустите проект с помощью Docker Compose:

```sh
docker-compose up --build