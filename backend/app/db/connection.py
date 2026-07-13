import oracledb

# Oracle Connection Details
USERNAME = "tradepilot"
PASSWORD = "Password1"
HOST = "localhost"
PORT = 1521
SERVICE_NAME = "FREEPDB1"


def get_connection():
    connection = oracledb.connect(
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        service_name=SERVICE_NAME
    )

    return connection