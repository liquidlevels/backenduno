from flask import Flask, request, jsonify
from query import user_query, users_query

app = Flask(__name__)

@app.route("/page")
def page():
    return "<p>estas en /page</p>"
@app.route("/test")
def test():
    return "<p>estas en /test</p>"

@app.route("/echo", methods=["POST"])
def echo():
    name = request.values.get("name")
    to_echo = request.values.get("echo")

    response = "hey karnalgas {}! dijiste {}".format(name, to_echo)

    return response

@app.route("/users", methods=["GET"])
def users():
    query = query.users_query()
    return jsonify(query), 200

@app.route("/user/<int:user_id>", methods=["GET"])
def user_by_id(user_id):
    user = user_query(user_id)
    if user:
        return jsonify(user), 200
    else:
        jsonify({"error": "user not found"}), 404
app.run()
