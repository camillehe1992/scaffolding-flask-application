from flask import Flask, make_response
from flask_cors import CORS
from server.controller import user
from server.controller.auth import token_required

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "Thisisasecret"


@app.route("/api/signup", methods=["POST"])
def user_signup():
    return user.signup()


@app.route("/api/login", methods=["POST"])
def user_login():
    return user.login(app)


@app.route("/api/users", methods=["GET"])
@token_required
def get_user(user):
    return make_response(user, 200)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
