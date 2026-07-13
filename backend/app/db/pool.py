import oracledb

from app.core.config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_SERVICE,
)

dsn = f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"

pool = None


def create_pool():
    global pool

    if pool is None:
        pool = oracledb.create_pool(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=dsn,
            min=2,
            max=5,
            increment=1,
        )

    return pool


def get_pool():
    return pool