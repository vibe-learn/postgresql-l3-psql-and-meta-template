"""Homework scaffold — postgresql lesson `l3_psql_and_meta` (Vibe Learn).

Задача: миграция из dump.sql, COPY из CSV, EXPLAIN ANALYZE (JSON) и экспорт среза в CSV.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

Драйвер: psycopg (v3). DSN берётся из env DATABASE_URL.
"""

import os

import psycopg


def database_url() -> str:
    """DSN PostgreSQL из env. Дефолт совпадает с docker-compose.yml."""
    return os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/postgres",
    )


def connect() -> "psycopg.Connection":
    """Открыть соединение psycopg из DATABASE_URL."""
    return psycopg.connect(database_url())


# ----- TODO #1: run_migration -----
def run_migration(conn, dump_sql_path: str) -> None:
    """прочитать dump.sql и выполнить через cursor.execute (или subprocess psql)"""
    raise NotImplementedError("run_migration: реализуй меня")


# ----- TODO #2: copy_csv_into -----
def copy_csv_into(conn, table: str, csv_path: str) -> int:
    """загрузить CSV через cursor.copy (COPY ... FROM STDIN), вернуть число строк"""
    raise NotImplementedError("copy_csv_into: реализуй меня")


# ----- TODO #3: explain_json -----
def explain_json(conn, sql: str, params: tuple = ()) -> dict:
    """EXPLAIN (ANALYZE, FORMAT JSON) и распарсить план в dict"""
    raise NotImplementedError("explain_json: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — postgresql lesson scaffold up")
    print(f"DATABASE_URL: {database_url()}")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
