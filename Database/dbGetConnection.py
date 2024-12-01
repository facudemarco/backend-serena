import mysql.connector

def getConnection():
    config = {
        'user': 'u830440565_facundo',
        'password': 'Iweb.2024!',
        'host': '190.49.91.171',
        'database': 'u830440565_mainDB_serena',
        'raise_on_warnings': True,
        'port': '8000'
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def getConnectionForLogin():
    config = {
        'user': 'u830440565_facundo',
        'password': 'Iweb.2024!',
        'host': '190.49.91.171',
        'database': 'u830440565_mainDB_serena',
        'raise_on_warnings': True,
        'table': 'credentials',
        'port': '8000'
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None