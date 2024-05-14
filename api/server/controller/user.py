import uuid
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from server.dao.user import UserDao
from flask import request, make_response


def signup():
    # Init UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    # Check for existing user
    existing_user = user_dao.get_uesr_by_email(email)
    if existing_user:
        response = make_response(
            {"success": False, "msg": "User already exists. Please Log in."}, 202
        )
    else:
        # Register the new user into database
        user_id = str(uuid.uuid4())
        user_dao.insert(
            user_id, username, email, generate_password_hash(password, method="pbkdf2")
        )
        response = make_response(
            {"success": True, "msg": "Registered successfully"}, 201
        )

    return response


def login(app):
    email = request.json.get("email")
    password = request.json.get("password")

    # Init UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()
    # Query user from database
    user_info = user_dao.get_uesr_by_email(email)

    # Validate user information
    if user_info and len(user_info) > 0:
        user = {
            "user_id": user_info[0][1],
            "username": user_info[0][2],
            "email": user_info[0][3],
        }
        if check_password_hash(user_info[0][4], password):
            # generates the JWT Token
            user["token"] = jwt.encode(
                {
                    "user_id": user.get("user_id"),
                    "exp": datetime.utcnow() + timedelta(minutes=30),
                },
                app.config["SECRET_KEY"],
            )
            print(user)

            response = make_response(
                {
                    "success": True,
                    "msg": "Login success.",
                    "user": user,
                },
                201,
            )

        else:
            response = make_response(
                {"success": False, "msg": "Invalid password."}, 403
            )
    else:
        response = make_response({"success": False, "msg": "User does not exist."}, 403)

        print(response)
    return response


def get_user(user_id):
    # Init UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()

    user_info = user_dao.get_user_by_id(user_id)
    if user_info and len(user_info) > 0:
        user = {
            "user_id": user_info[0][1],
            "username": user_info[0][2],
            "email": user_info[0][3],
            "active": user_info[0][5],
        }
        return user
    return {}
