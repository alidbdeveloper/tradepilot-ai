from connection import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("select sysdate from dual")

for row in cursor:
    print(row)

cursor.close()
connection.close()