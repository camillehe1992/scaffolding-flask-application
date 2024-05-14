import mysql.connector


class UserDao:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            self.connection.commit()
            print("Executed SQL: ", cursor.statement)
            return result
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            raise e

    def insert(self, user_id, username, email, password):
        query = "INSERT INTO user (user_id, username, email, password) VALUES (%s, %s, %s, %s)"
        values = (user_id, username, email, password)
        self.execute_query(query, values)

    def update(self, user_id, username, password):
        query = "UPDATE user SET username = %s, password = %s WHERE id = %s"
        values = (username, password, user_id)
        self.execute_query(query, values)

    def delete(self, user_id):
        query = "DELETE FROM user WHERE user_id = %s"
        values = (user_id,)
        self.execute_query(query, values)

    def get_all_users(self):
        query = "SELECT * FROM user"
        return self.execute_query(query)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM user WHERE user_id = %s"
        values = (user_id,)
        return self.execute_query(query, values)

    def get_user_by_username(self, username):
        query = "SELECT * FROM user WHERE username = %s"
        values = (username,)
        return self.execute_query(query, values)

    def get_uesr_by_email(self, email):
        query = "SELECT * FROM user WHERE email = %s"
        values = (email,)
        return self.execute_query(query, values)
