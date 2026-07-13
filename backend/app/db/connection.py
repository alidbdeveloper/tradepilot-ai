from app.db.pool import get_pool


def get_connection():
    pool = get_pool()

    if pool is None:
        raise Exception("Database pool has not been initialized.")

    return pool.acquire()