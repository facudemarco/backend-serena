import mysql.connector

def getConnection():
    config = {
        'user': 'facundo',
        'password': 'Iweb.2024!',
        'host': '190.49.91.171',
        'database': 'u830440565_mainDB_serena',
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
        'user': 'facundo',
        'password': 'Iweb.2024!',
        'host': '190.49.91.171',
        'database': 'u830440565_mainDB_serena',
        'raise_on_warnings': True,
        'table': 'credentials'
    }

    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None