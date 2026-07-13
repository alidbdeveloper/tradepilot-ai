from app.db.pool import create_pool
from app.db.connection import get_connection

create_pool()

connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT SYSDATE FROM dual")

for row in cursor:
    print(row)

cursor.close()
connection.close()