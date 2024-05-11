from server.dao.user import UserDao
from flask import request, jsonify


def register():
    # 初始化 UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()
    # 获取请求参数
    username = request.json.get("username")
    password = request.json.get("password")

    # 检查用户名是否已存在
    existing_user = user_dao.get_user_by_username(username)
    print(existing_user)
    if existing_user:
        response = {"success": False, "msg": "User already exists"}
    else:
        # 在数据库中注册新用户
        user_dao.insert(username, password)
        response = {"success": True, "msg": "Registered successfully"}

    return jsonify(response)


def login():
    # 获取请求参数
    username = request.json.get("username")
    password = request.json.get("password")

    # 初始化 UserDao
    user_dao = UserDao(
        host="127.0.0.1", user="root", password="mysql123", database="demo"
    )
    user_dao.connect()
    # 从数据库中查询用户信息
    user_info = user_dao.get_user_by_username(username)
    print(user_info)

    # 验证用户信息
    if user_info and len(user_info) > 0:
        stored_password = user_info[0][2]
        if password == stored_password:
            # 登录成功
            response = {"success": True, "msg": "Login success"}
        else:
            # 密码错误
            response = {"success": False, "msg": "Password is invalid"}
    else:
        # 用户不存在
        response = {"success": False, "msg": "User does not exist"}

    return jsonify(response)
