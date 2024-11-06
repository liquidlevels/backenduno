from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello im Emmanuel</p>"

@app.route("/comoquieran")
def psql_select():
#codigo para hacer un select en psql
