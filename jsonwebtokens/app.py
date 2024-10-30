from datetime import timedelta

from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "d1f81206a6e31186dfc6e22ac6301e552ee90e0bee3061d3a036708a8eb62155"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)

users = []

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"msg": "username, password are required"}), 400

    if any(user["username"] == username for user in users):
        return jsonify({"msg": "user already exists"}), 409

    users.append({"username": username, "password": password})
    return jsonify({"msg": "registered successfully"}), 201


# We verify the users password here, so we are returning a fresh access token
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = next((user for user in users if user["username"] == username and user["password"] == password), None)
    if not user:
        return jsonify({"msg": "wrong username or password"}), 401

    access_token = create_access_token(identity=username, fresh=True)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


# If we are refreshing a token here we have not verified the users password in
# a while, so mark the newly created access token as not fresh
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)


# Only allow fresh JWTs to access this route with the `fresh=True` arguement.
@app.route("/protected", methods=["GET"])
@jwt_required(fresh=True)
def protected():
    return jsonify(msg="soy digno")


if __name__ == "__main__":
    app.run()
