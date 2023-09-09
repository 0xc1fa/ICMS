import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from dotenv import load_dotenv

_connection = None

def init_connection():
    global _connection
    load_dotenv()
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    _connection = QSqlDatabase.addDatabase("QMYSQL")
    _connection.setHostName(DB_HOST)
    _connection.setUserName(DB_USER)
    _connection.setPassword(DB_PASSWORD)
    _connection.setDatabaseName(DB_NAME)
    if not _connection.open():
        print("Error: connection failed")


def fetch_data(self, query):
    global connection
    if not connection:
        assert False, "Call init_connection() before calling fetch_data()"
    query = QSqlQuery(query)
    while query.next():
        record = query.record()
        yield [record.value(field_name) for field_name in record.fieldNames()]


def get_connection():
    global _connection
    return _connection


def close_connection():
    global _connection
    _connection.close()
    _connection = None
