# nginx como reverse proxy con flask

## Docker

comando para crear un contenedor de nginx con la ultima version, name se cambia por el nombre que le pondras a tu contenedor
```
sudo docker run --name name -d -p 80:80 nginx:latest
```

con este comando puedes verificar que tu contenedor esta corriendo
```
sudo docker ps
```

una vez verificamos que este corriendo, ponemos el siguiente comando para ejecutar una instancia de bash dentro del contenedor
> **Nota:** puedes utilizar el **nombre** o **id**  
```
sudo docker exec -it name /bin/bash
```

## Configuracion inicial

dentro de la instancia de bash ponemos el siguiente comando
```
apt update
```

ahora instalamos los paquetes dev y venv de python3 en su version 11
```
apt install python3.11-dev
apt install python3.11-venv
```

ahora instalamos vim o algun editor de texto
```
apt install vim
```
creamos un usuario
```
adduser [user]
```
una vez creado el usuario, navegamos a la carpeta del usuario
> **Nota:** se cambia la palabra user por el nombre de tu usuario
```
cd /home/user/
```

una vez dentro de la carpeta del usuario, creamos una carpeta para trabajar con python
```
mkdir py
cd py/
```

## Configuracion de flask

### virtual environment

creamos nuestro virtual environment para despues activarlo
```
python3 -m venv venv
source venv/bin/activate
```

una vez activado el venv, instalamos flask
```
pip install flask
```

en nuestro editor de texto abrimos/creamos un archivo llamado hello.py
```
vim hello.py
```

siguiendo los pasos de la pagina oficial de flask

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

- creamos una variable de entorno con **export**
- corremos nuestra instancia de flask
```
export FLASK_APP=hello
flask run --host=0.0.0.0
```
