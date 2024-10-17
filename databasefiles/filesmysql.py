import json
import mysql.connector
from mysql.connector import Error

config = {
    'user': 'root',
    'password': 'liQuid?sql2',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'magic'
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_json_data(connection, json_file):
    with open(json_file) as f:
        data = json.load(f)
        cursor = connection.cursor()
        
        for item in data:
            sql = """
            INSERT INTO files (id, uri, type, name, description, download_uri, updated_at, size, content_type, content_encoding) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                item.get('id'),
                item.get('uri'),
                item.get('type', None),
                item.get('name', None),
                item.get('description', None),
                item.get('download_uri', None),
                item.get('updated_at', None),
                item.get('size', None),
                item.get('content_type', None),
                item.get('content_encoding', None)
            ))

        connection.commit()
        print(f"{cursor.rowcount} records inserted.")

if __name__ == "__main__":
    conn = connect_to_database()
    if conn:
        insert_json_data(conn, 'data.json')
        conn.close()

