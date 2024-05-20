from flask import Flask, make_response
from flask_cors import CORS
from server.controller.auth import token_required, Auth
from server.utils.otp import OTPGenerator
from server.utils.smtp import SMTPClient

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "Thisisasecret"


@app.route("/auth/register", methods=["POST"])
def register():
    auth = Auth()
    return auth.register()


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
    app.run(debug=True, port=5000)
