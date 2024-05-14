from flask import Flask
from flask_cors import CORS
from server.controller import user

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "Thisisasecret"


@app.route("/api/signup", methods=["POST"])
def user_signup():
    return user.signup()


@app.route("/api/login", methods=["POST"])
def user_login():
    return user.login(app)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
