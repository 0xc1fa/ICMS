from PySide6.QtSql import QSqlDatabase, QSqlQuery

import providers.DatabaseProvider as db_provider

_user = None

def get_user():
    global _user
    db_provider.init_connection()
    db = db_provider.get_connection()
    
    return _user

class UserProvider:
    def __init__(self, database_provider, username):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName(hostname)
        self.db.setDatabaseName(db_name)
        self.db.setUserName(username)
        self.db.setPassword(password)
        if not self.db.open():
            print("Error: connection failed")
            
    def fetch_data(self, query):
        query = QSqlQuery(query)
        while query.next():
            record = query.record()
            yield [record.value(field_name) for field_name in record.fieldNames()]
