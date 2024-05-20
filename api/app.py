from flask import Flask, make_response
from flask_cors import CORS
from server.controller.auth import token_required, Auth
from config import LocalConfig

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "Thisisasecret"
app.config["SECURITY_PASSWORD_SALT"] = "Thisisasecret"

app.config["DB_HOST"] = "127.0.0.1"
app.config["DB_USER"] = "root"
app.config["DB_PASS"] = "mysql123"
app.config["DB_NAME"] = "demo"
app.config["SMTP_HOST"] = "localhost"
app.config["SMTP_PORT"] = 2525
app.config["SMTP_USER"] = "no-reply@example.com"


@app.route("/auth/register", methods=["POST"])
def register():
    auth = Auth()
    return auth.register()


@app.route("/auth/confirm/<token>", methods=["GET"])
def confirm_email(token):
    auth = Auth()
    return auth.confirm_token(token)


@app.route("/auth/login", methods=["POST"])
def login():
    auth = Auth()
    return auth.login()


@app.route("/auth/user", methods=["GET"])
@token_required
def get_user(user):
    return make_response(user, 200)


@app.route("/auth/send-code", methods=["POST"])
def send_code():
    auth = Auth()
    return auth.send_code()


@app.route("/auth/reset-password", methods=["POST"])
def reset_password():
    auth = Auth()
    return auth.reset_password()


if __name__ == "__main__":
    # app.config.from_object(LocalConfig())
    app.run(debug=True, port=5000)
