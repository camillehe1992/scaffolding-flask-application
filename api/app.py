from flask import Flask
from flask_cors import CORS  # 引入 CORS 模块
from server.controller import user

app = Flask(__name__)
CORS(app)  # 在应用中使用 CORS

app.config["SECRET_KEY"] = "Thisisasecret"


@app.route("/api/register", methods=["POST"])
def user_register():
    return user.signup()


# 定义用户登录接口
# 用户登录接口
@app.route("/api/login", methods=["POST"])
def user_login():
    return user.login(app)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
