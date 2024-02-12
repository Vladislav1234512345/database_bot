import mysql.connector

from config import database_settings

def create_users_table():
    sql_query = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,user_id INT UNIQUE,login VARCHAR(100) NOT NULL,password VARCHAR(50) NOT NULL)"
    execute_sql_query(sql_query)

def insert_into_users_table(login: str, password: str, user_id):
    sql_query = f"INSERT INTO users (login, password, user_id) VALUES ('%s', '%s', '%s')" % (login, password, user_id)
    execute_sql_query(sql_query)
def execute_sql_query(sql_query: str):

    database_config = {
        "user": database_settings.username,
        "password": database_settings.password,
        "host": database_settings.localhost,
        "database": database_settings.database,
    }

    connector = mysql.connector.connect(**database_config)

    cursor = connector.cursor()

    cursor.execute(sql_query)

    connector.commit()

    cursor.close()
    connector.close()

def fetchall_sql_query(sql_query: str):
    database_config = {
        "user": database_settings.username,
        "password": database_settings.password,
        "host": database_settings.localhost,
        "database": database_settings.database,
    }

    connector = mysql.connector.connect(**database_config)

    cursor = connector.cursor()

    cursor.execute(sql_query)

    return cursor.fetchall()