
dentro de un *compose.yaml*
```
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

crear un archivo *app.py* y pegar:
```
```

dentro de *Dockerfile*
```
FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN apt update
RUN apt install git
#RUN git clone [url]
COPY requerimientos.txt .
RUN pip install -r requerimientos.txt
COPY app.py .
CMD ["flask","run","--host","0.0.0.0"]
```

