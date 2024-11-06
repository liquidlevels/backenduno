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
