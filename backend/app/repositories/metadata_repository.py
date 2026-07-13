from app.db.connection import get_connection


def get_all_tables():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT table_name
        FROM user_tables
        ORDER BY table_name
    """)

    tables = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return tables