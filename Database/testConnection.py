import mysql.connector

def get_connection():
    config = {
        'user': 'u830440565_facundo',
        'password': 'Iweb.2024!',
        'host': '193.203.175.121',
        'database': 'u830440565_mainDB_serena',
        'raise_on_warnings': True,
        'port': '3306'
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        conn.close()
