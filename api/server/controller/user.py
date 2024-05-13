from server.dao.user import UserDao
from flask import request, jsonify


def register():
    # Init UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    # Check if the email exists
    existing_user = user_dao.get_uesr_by_email(email)
    print(existing_user)
    if existing_user:
        response = {"success": False, "msg": "User already exists"}
    else:
        # Register the new user into database
        user_dao.insert(username, email, password)
        response = {"success": True, "msg": "Registered successfully"}

    return jsonify(response)


def login():
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
        stored_password = user_info[0][5]
        if password == stored_password:
            response = {"success": True, "msg": "Login success"}
            print("Login success")
        else:
            response = {"success": False, "msg": "Invalid password"}
    else:
        response = {"success": False, "msg": "User is not found"}

        print(response)
    return jsonify(response)
