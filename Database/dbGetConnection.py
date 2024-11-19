import mysql.connector

def getConnection():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'db_test',
        'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def getConnectionForLogin():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'db_credentials',
        'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None