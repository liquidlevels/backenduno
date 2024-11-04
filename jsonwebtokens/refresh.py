from datetime import timedelta

from flask import Flask, request, jsonify, redirect, url_for

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from query import insert_user, get_userid_by_username, get_password, get_username, insert_tokens
import bcrypt

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "d1f81206a6e31186dfc6e22ac6301e552ee90e0bee3061d3a036708a8eb62155"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=2)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=5)
jwt = JWTManager(app)

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if not username or not password:
        return jsonify({"msg": "username, password are required"}), 400

    if get_username(username):
        return jsonify({"msg": "user already exists"}), 409
    
    pw = str.encode(password)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw, salt)
    insert_user(username, hashed)

    return jsonify({"msg": "registered successfully"}), 201


# We verify the users password here, so we are returning a fresh access token
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    user_exists = get_username(username)
    if not user_exists:
        return jsonify({"msg": "wrong username"}), 401
    else:
        user_password = get_password(username)
        byte_data = bytes(user_password[0])
        
        isSamePassword = bcrypt.checkpw(password.encode('utf-8'), byte_data)
        
        if not isSamePassword:
            return jsonify({"msg": "wrong password"}), 401
        else:
            access_token = create_access_token(identity=username, fresh=True)
            refresh_token = create_refresh_token(identity=username)
            
            userinfo = get_userid_by_username(username)
            user_id = userinfo[0]
            insert_tokens(user_id, access_token, refresh_token)

            return jsonify(access_token=access_token, refresh_token=refresh_token)
            
    return jsonify({"message": "ok"}), 200


# If we are refreshing a token here we have not verified the users password in
# a while, so mark the newly created access token as not fresh
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":
    app.run()
