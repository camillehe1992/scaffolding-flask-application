from server.dao.user import UserDao


class User:
    def __init__(self) -> None:
        self.user_dao = UserDao(
            host="127.0.0.1", user="root", password="mysql123", database="demo"
        )
        self.user_dao.connect()

    def get_user_by_id(self, user_id):
        user_info = self.user_dao.get_user_by_id(user_id)
        if user_info and len(user_info) > 0:
            user = {
                "user_id": user_info[0][1],
                "username": user_info[0][2],
                "email": user_info[0][3],
                "active": user_info[0][5],
                "access_token": user_info[0][6],
            }
            return user
        return None

    def get_user_by_email(self, email):
        user_info = self.user_dao.get_uesr_by_email(email)
        if user_info and len(user_info) > 0:
            user = {
                "user_id": user_info[0][1],
                "username": user_info[0][2],
                "email": user_info[0][3],
                "active": user_info[0][5],
                "access_token": user_info[0][6],
            }
            return user
        return None

    def update_username(self, user_id, username):
        user_info = self.user_dao.update_username(user_id, username)
        return user_info

    def update_password(self, user_id, password):
        user_info = self.user_dao.update_password(user_id, password)
        return user_info
