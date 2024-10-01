# Instalacion y configuracion de *postgresql* en *docker*

Descargar la imagen de postgres
```
docker pull postgres
```

Crear un contenedor con la imagen de postgres
```
docker run -d \
	--name some-postgres \
	-e POSTGRES_PASSWORD=mysecretpassword \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-p 5432:5432 \
	postgres
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

desde su dispositivo, copiar el archivo *.json* dentro del contenedor
> **Nota:** *path* se refiere a donde se encuentra el archivo *.json* (ejemplo: ~/Downloads/data.json), *contenedor* puedes utilizar id o nombre
```
docker cp path contenedor:/home
```

## Configuracion de postgres

entrar a *psql* directamente dentro del contenedor
> **Nota:** en *name* puedes utilizar el id o nombre del contenedor
```
docker exec -it name psql -h localhost -U postgres -p 5432
```

crear una base de datos, en este caso *magic*
```
CREATE DATABASE magic;
```

cambiamos a *magic* para manipular la base de datos
```
\c magic
```

creamos tabla *files*
```
CREATE TABLE files (
    id UUID PRIMARY KEY,
    uri TEXT NOT NULL,
    type VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    description TEXT,
    download_uri TEXT,
    updated_at TIMESTAMP,
    size INTEGER,
    content_type VARCHAR(255),
    content_encoding VARCHAR(50)
);
```

## Configuracion dentro del contenedor

ejecuta una instancia de *bash* de tu contenedor
> **Nota:** en *name* puedes utilizar el id o nombre del contenedor
```
docker exec -it name /bin/bash
```

actualiza los repositorios apt
```
apt update
```
instala lo siguiente:
```
apt install vim
apt install python3.11-dev
apt install python3-psycopg2
apt install python3 mysql-connector-python
```

dentro de */home*:
```
vim table.py
```

pegar en *table.py*
> **Nota** no olvidar cambiar *yourpass* por su password de postgres
```
import json
import psycopg2

json_file_path = 'data.json'

conn = psycopg2.connect(database="magic", user="postgres", password="yourpass", host="localhost", port="5432")
cursor = conn.cursor()

with open(json_file_path, 'r') as f:
    data = json.load(f)

insert_query = """
    INSERT INTO files (id, uri, type, name, description, download_uri, updated_at, size, content_type, content_encoding)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for record in data:
    cursor.execute(insert_query, (
        record.get('id'),
        record.get('uri'),
        record.get('type', 'unknown'),
        record.get('name'), 
        record.get('description'),
        record.get('download_uri'),
        record.get('updated_at'),
        record.get('size', 0),
        record.get('content_type', 'unknown'),
        record.get('content_encoding', 'none')
    ))

conn.commit()

cursor.close()
conn.close()

print("Data inserted successfully into PostgreSQL table.")

```

## Confirmar que los datos se importaron correctamente

en la instancia de postgres que iniciamos en *Configuracion de postgres*:
```
SELECT * from files;
```

