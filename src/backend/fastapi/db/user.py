from .utils import query, cur

class USERDB(object):
    def __init__(self):
        pass
    def fit(self):
        self.create_user()
    def create_user(self):
        create_query = """
        CREATE TABLE IF NOT EXISTS D_USER (
        id SERIAL PRIMARY KEY,
        USER_NAME VARCHAR UNIQUE,
        PASSWORD VARCHAR NOT NULL
        );
        """
        query(create_query)
        print("Done create user table")
    def insert_user(self, user_name, password):
        q = f""" 
INSERT INTO D_USER(user_name, password)
VALUES
(%(user_name)s, %(password)s)
        """
        values = {"user_name": user_name,
                  "password": password}
        query(q, values)
        return True
    def validate_user(self, user_name, password):
        q = f""" 
        SELECT
        distinct
        user_name,
        password 
        FROM D_USER
        where 1=1
        and user_name = '{user_name}'
        and password = '{password}'

        """
        cur.execute(q)
        output = cur.fetchall()
        print(output)
        if len(output) > 0:
            return True
        return False

userdb = USERDB()
