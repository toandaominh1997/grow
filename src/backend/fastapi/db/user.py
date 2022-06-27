from .utils import PostgresSQL

class USERDB(object):
    def __init__(self):
        self.pg = PostgresSQL()
    def fit(self):
        self.create_user()
    def create_user(self):
        query_string = """
        CREATE TABLE IF NOT EXISTS D_USER (
        id SERIAL PRIMARY KEY,
        USER_NAME VARCHAR UNIQUE,
        PASSWORD VARCHAR NOT NULL
        );
        """
        cur = self.pg.query(query_string)
        if cur:
            print('Done Create User Table')
        else:
            print('InCompleted Create UserTable')
    def insert_user(self, user_name, password):
        q = f""" 
INSERT INTO D_USER(user_name, password)
VALUES
(%(user_name)s, %(password)s)
        """
        values = {"user_name": user_name,
                  "password": password}
        cur = self.pg.query(q, values)
        return cur
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
        cur = self.pg.query(q)
        output = cur.fetchone()
        return output
