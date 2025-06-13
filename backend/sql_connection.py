import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx

    if __cnx is None or not __cnx.is_connected():
        __cnx = mysql.connector.connect(
            user='root',
            password='Chamodi@2003',
            host='localhost',
            database='grocery'
        )

    return __cnx
