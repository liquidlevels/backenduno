# Instalacion y configuracion de *mysql* en *docker*

Descargar la imagen de mysql
```
docker pull mysql/mysql-server:latest
```

Crear un contenedor con la imagen de mysql
```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql:latest
```

# Importacion de datos

ve al sitio
```
https://scryfall.com/docs/api/bulk-data
```

descarga lo siguiente

![File](/images/file.png)

informacion en la que se basa para crear la tabla dentro de la base de datos
![Info](/images/info.png)

cambiar el nombre del archivo descargado a *data.json*

## Configuracion de mysql

entrar a una instancia de *mysql* dentro del contenedor
> **Nota:** en *name* puedes usar el id o nombre del conenedor
```
docker exec -it name mysql -u root -p
```

crear base de datos
```
CREATE DATABASE magic;
```

entramos a *magic*
```
USE magic;
```

creamos la tabla *files*
```
CREATE TABLE files (
    id CHAR(36) PRIMARY KEY,
    uri TEXT NOT NULL,
    type VARCHAR(255) NULL,
    name VARCHAR(255),
    description TEXT,
    download_uri TEXT,
    updated_at TIMESTAMP,
    size INT,
    content_type VARCHAR(255),
    content_encoding VARCHAR(50)
);
```

## Configuracion para la importacion de datos


- crear una carpeta de trabajo
- mover el archivo *data.json* que descargo, a la carpeta de trabajo

dentro de un virtual environment de python:
``` 
pip install mysql-connector-python
```

dentro de un archivo *.py*:
> **Nota:** no olvide modificar en *config*: password, database
```
import json
import mysql.connector
from mysql.connector import Error

config = {
    'user': 'root',
    'password': 'my-secret-pw',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'mydatabase'
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
```

## Confirmar que los datos se importaron correctamente

en la instancia de mysql que iniciamos en *Configuracion de mysql*:
```
SELECT * FROM files;
```
