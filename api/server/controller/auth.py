from functools import wraps
import uuid
import jwt
from datetime import datetime, timedelta
from flask import request, abort, current_app, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from server.dao.user import UserDao

from server.controller.user import User
from server.utils.otp import OTPGenerator
from server.utils.smtp import SMTPClient


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized",
            }, 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            user = User()
            current_user = user.get_user_by_id(data["user_id"])

            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized",
                }, 401
            if not current_user["active"]:
                abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e),
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated


class Auth:
    def __init__(self) -> None:
        self.app = current_app
        self.user_dao = UserDao(
            host="127.0.0.1", user="root", password="mysql123", database="demo"
        )
        self.user = User()
        self.user_dao.connect()

    def register(self):
        username = request.json.get("email")
        email = request.json.get("email")
        password = request.json.get("password")

        # Check for existing user
        user_info = self.user_dao.get_uesr_by_email(email)
        if user_info and len(user_info) > 0:
            response = make_response(
                {"message": "User already exists. Please Log in."}, 400
            )
        else:
            # Register the new user into database
            user_id = str(uuid.uuid4())

            # generates the JWT Token
            access_token = jwt.encode(
                {
                    "user_id": user_id,
                    "exp": datetime.utcnow() + timedelta(minutes=5),
                },
                self.app.config["SECRET_KEY"],
            )

            self.user_dao.insert(
                user_id,
                username,
                email,
                generate_password_hash(password, method="pbkdf2"),
                access_token,
            )
            response = make_response(
                {
                    "user_name": username,
                    "email": email,
                    "access_token": access_token,
                },
                201,
            )

        return response

    def login(self):
        email = request.json.get("email")
        password = request.json.get("password")

        # Query user from database
        user_info = self.user_dao.get_uesr_by_email(email)

        # Validate user information
        if user_info and len(user_info) > 0:
            user = {
                "username": user_info[0][2],
                "email": user_info[0][3],
            }
            if check_password_hash(user_info[0][4], password):
                # generates the JWT Token
                user["access_token"] = jwt.encode(
                    {
                        "user_id": user_info[0][1],
                        "exp": datetime.utcnow() + timedelta(minutes=5),
                    },
                    self.app.config["SECRET_KEY"],
                )
                self.user_dao.refresh_token(user_info[0][1], user["access_token"])

                response = make_response(
                    user,
                    201,
                )

            else:
                response = make_response({"message": "Invalid password."}, 403)
        else:
            response = make_response({"message": "User does not exist."}, 403)
        return response

    def send_code(self):
        email = request.json.get("email")

        user = self.user.get_user_by_email(email)
        if not user:
            return {"message": "The user does not exist. Please check!"}, 400

        generator = OTPGenerator()
        code = generator.generate_code()

        mail_message = {
            "subject": "Verify your new account",
            "body": f"The verification code to your new account is {code}",
            "to": email,
        }
        client = SMTPClient(**mail_message, debug=False)
        res = client.send_email()

        if res:
            return {"message": "Email is sent out!"}, 200

        return {"message": "Failed to send verification code"}, 400

    def reset_password(self):
        code = request.json.get("code")
        email = request.json.get("email")
        password = request.json.get("password")

        user = self.user.get_user_by_email(email)
        if not user:
            return {"message": "The user does not exist. Please check"}, 400

        generator = OTPGenerator()
        if not generator.verify_code(code):
            return {"message": "The code is expired. Please resend"}, 400

        hashed_password = generate_password_hash(password, method="pbkdf2")
        self.user_dao.update_password(user.get("user_id"), hashed_password)

        return {"message": "Password reset successfully"}, 200
