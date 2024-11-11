# Асинхронный клиент для биржи

## Стек технологий  

![Static Badge](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)
  ![Static Badge](https://img.shields.io/badge/FastAPI-0.115.4-%23009688?logo=FastAPI)
![Static Badge](https://img.shields.io/badge/Aiohttp-3.10.10-%232C5BB4?logo=aiohttp)
![Static Badge](https://img.shields.io/badge/SQLAlchemy-2.0.36-%23D71F00?logo=sqlalchemy)
 ![Static Badge](https://img.shields.io/badge/Gunicorn-2.32.0-%23499848?logo=gunicorn)
![Static Badge](https://img.shields.io/badge/Pydantic-2.9.2-%23E92063?logo=pydantic)
 ![Static Badge](https://img.shields.io/badge/Docker-27.2.1-blue?logo=docker)
 ![Static Badge](https://img.shields.io/badge/DockerCompose-1.25.3-blue?logo=docker)
 ![Static Badge](https://img.shields.io/badge/Postgresql-16.4.1-blue?logo=postgresql) 
 ![Static Badge](https://img.shields.io/badge/dotenv-1.0.1-%23ECD53F?logo=dotenv) 
 ![Static Badge](https://img.shields.io/badge/Poetry-0.1.0-%2360A5FA?logo=poetry)

## Установка проекта локально (Linux)  
+ Склонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/lobster2nd/async_crypto.git  
cd async_crypto 
```

+ Создать файл .env, задав значения переменным POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER  
  Например:
```
POSTGRES_DB=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
```

+ Запуск сервера:  

```
make up
```

+ Остановить сервер:  

```
make down
```

+ Документация
```
http://127.0.0.1:8000/docs/
```

## ТЗ

1. Написать для криптобиржи Deribit (https://docs.deribit.com/)
асинхронный клиент на aiohhtp. Клиент должен каждую минуту забирать
с биржи текущую цену btc_usd и eth_usd (index price валюты) после
чего сохранять в базу данных тикер валюты, текущую цену и время в
UNIX timestamp.
2. Написать внешнее API для обработки сохраненных данных на FastAPI.
Обязательные требования:
1. API должно включать в себя следующие методы:
- Получение всех сохраненных данных по указанной валюте
- Получение последней цены валюты
- Получение цены валюты с фильтром по дате
Все методы должны быть GET и у каждого метода дожен быть
обязятельный query-параметр "ticker".
2. Код выложить на гитхаб с подробным readme и документацией по
разворачиванию.
Можно использовать любую БД на выбор для хранения цен.
