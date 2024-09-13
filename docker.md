# nginx como reverse proxy con flask

## Docker

creamos un contenedor de nginx con la ultima version, **name** se cambia por el nombre que le pondras a tu contenedor
```
sudo docker run --name name -d -p 80:80 nginx:latest
```

con este comando puedes verificar que tu contenedor esta corriendo:
```
sudo docker ps
```

una vez verificamos que este corriendo, ponemos el siguiente comando para ejecutar una instancia de bash dentro del contenedor
> **Nota:** puedes utilizar el **nombre** o **id**  
```
sudo docker exec -it name /bin/bash
```

## Configuracion inicial

dentro de la instancia de bash actualizamos los repositorios con:
```
apt update
```

ahora se instala los paquetes **dev** y **venv** de **python3** en su version **11**
```
apt install python3.11-dev
apt install python3.11-venv
```

instalamos algun editor de texto, en mi caso **vim**:
```
apt install vim
```
## Configuracion de nginx

verifica que nginx este funcionando poniendo el siguiente url en el navegador
```
http://localhost:80
```

edite el *index.html* dentro de:
```
/usr/share/nginx/html/
```

edite la configuracion de nginx *nginx.conf* dentro de:
```
/etc/nginx/
```
agrega la seccion dentro de la seccion *http{}* para escuchar el puerto **80** redirigir el trafico hacia el puerto **5000** y como host, tenemos **127.0.0.1** o **localhost**
```
server {
    listen       80;
    server_name 127.0.0.1;

      location /page {
    	proxy_pass http://127.0.0.1:5000;
      }
      location /test {
      	proxy_pass http://172.17.0.2:5000;
      }
      location / {
      	root /usr/share/nginx/html;
	index index.html;
      }
    }
```

para que no haya problemas con la configuracion, borra **default.conf**:
```
etc/nginx/conf.d/
rm default.conf
```

salimos del contenedor utilizando **exit**:
```
root@41372ba75f40:/# exit
```

ahora reinicia el contenedor
```
docker restart [name o id]
```

instancia un bash dentro del contenedor:
```
sudo docker exec -it name /bin/bash
```

creamos un usuario
```
adduser [user]
```
una vez creado el usuario, navegamos a la carpeta del usuario
> **Nota:** se cambia la palabra **user** por el nombre de tu usuario
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

dentro de */home/user/py* creamos nuestro virtual environment para despues activarlo
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

@app.route('/page')
def page():
    return "<p>estas en /page</p>"
```

- creamos una variable de entorno con **export**
- corremos nuestra instancia de flask
```
export FLASK_APP=hello
flask run --host=0.0.0.0
```

ahora verificamos en el navegador que el reverse proxy funciona:
```
http://127.0.0.1:80/page
```
