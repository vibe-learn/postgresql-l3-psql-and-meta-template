        # postgresql — psql, мета-команды и инструменты

        Homework-шаблон для урока **l3_psql_and_meta** (psql, мета-команды и инструменты) на платформе Vibe Learn.

        ## Что делать

        Дано: пустая БД. Реализуй Python-скрипт (psycopg / asyncpg), который:
1) запускает миграцию из dump.sql (через subprocess psql либо чтение и cursor.execute);
2) загружает CSV в таблицу events через COPY (через psycopg copy_expert или asyncpg.copy_records_to_table);
3) выполняет EXPLAIN ANALYZE для целевого запроса и парсит JSON-формат плана;
4) экспортирует срез данных в CSV.
Тесты в template репо проверят: правильность парсинга плана, корректность COPY (число строк),
обработку ошибок миграции.

## Контекст (из transfer-задачи урока)

Production-инцидент: жалуется аналитика, что «отчёт по заказам показывает странные
данные за вчера». Тебя зовут разобраться. У тебя ssh-доступ к bastion и оттуда psql
к prod-replica (read-only). У тебя нет GUI, нет dashboard, нет grep по коду.

Тебе нужно:
1) Понять структуру таблицы `orders` (какие колонки, типы, что есть индекс по created_at?)
2) Узнать, сколько заказов за вчера и какой их status-distribution.
3) Посмотреть, как PG планирует выполнить тот самый «странный» запрос аналитика:
   `SELECT date_trunc('hour', created_at), sum(total_cents) FROM orders
    WHERE created_at >= now()::date - 1 GROUP BY 1 ORDER BY 1;`
4) Сохранить срез последних 1000 заказов в CSV для коллеги-аналитика.

## Recap из урока

- **psql — твой главный инструмент.** ORM и GUI — это надстройки; в инциденте у тебя ssh + psql, и этого достаточно.
- **`\d <name>` — первая команда** при разборе любой таблицы: колонки, типы, индексы, FK, constraint-ы — в одном выводе.
- **EXPLAIN (без ANALYZE)** — план, ничего не выполняется. **EXPLAIN ANALYZE** — выполняет и измеряет; осторожно с DML, обычно в транзакции.
- **COPY в 10-100× быстрее INSERT-цикла** для bulk-загрузки. `\copy` — клиентский, `COPY` — серверный с правами superuser.
- **pg_dump = логический бэкап** (SQL), удобен для small/medium и миграций. Для физического бэкапа всего кластера — pg_basebackup (M4).

        ## Как работать

        1. Платформа Vibe Learn создаёт копию этого репо в твоём GitHub-аккаунте по клику «Начать домашку» на странице урока (через GitHub `/generate`, codecrafters-pattern).
        2. Склонируй копию локально, реализуй TODO в `main.py`, прогони тесты, запушь.
        3. CI (`.github/workflows/ci.yml`) ставит зависимости и запускает `pytest` на каждый push. Платформа слушает результат через webhook от GitHub Actions и обновляет статус домашки на странице урока.

        ## Локальное окружение

        - Python 3.12+
        - Docker + docker-compose — `docker compose up -d` поднимает single-node PostgreSQL 16 на `localhost:5432` с healthcheck. DSN: `postgresql://postgres:postgres@localhost:5432/postgres`. Переопределяется через env `DATABASE_URL`.

        ## Запуск

        ```bash
        # Поднять локальный PostgreSQL
        docker compose up -d

        # Установить зависимости
        pip install -r requirements.txt

        # Прогнать тесты (интеграционный включается через PG_INTEGRATION=1)
        pytest
        PG_INTEGRATION=1 pytest

        # Запустить main (печатает marker; замени stub на реализацию)
        python main.py
        ```

        ## Заметка автора

        Это baseline-шаблон, сгенерированный платформой. Бизнес-сущность задачи (что конкретно реализовать в `main.py`, какие тесты сделать строгими) расширяется по ходу итераций — параллельно с углублением теории урока.
