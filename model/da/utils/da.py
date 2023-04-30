import mysql.connector

class DataAccess:
    def set_connection_string(self, host, user_name, password, database):
        self._host = host
        self._user_name = user_name
        self._password = password
        self._database = database

    def _connect(self):
        self._database = mysql.connector.connect(host=self._host,
                                                 user=self._user_name,
                                                 password=self._password,
                                                 database=self._database)
        self._cursor = self._database.cursor()

    def _disconnect(self):
        self._cursor.close()
        self._database.close()

    def transaction(self, sql_command, data):
        self._connect()
        if data:
            self._cursor.execute(sql_command, data)
        else:
            self._cursor.execute(sql_command)
        self._database.commit()
        self._disconnect()

    def find(self, sql_command, data=None):
        self._connect()
        if data:
            self._cursor.execute(sql_command, data)
        else:
            self._cursor.execute(sql_command)
        result = self._cursor.fetchall()
        self._disconnect()
        return result
