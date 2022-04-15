import psycopg2

class CREATE(object):
    def __init__(self):
        self.conn = psycopg2.connect(database = "database", user = "user", password = "password", host = "postgres", port = "5432")
        self.cur = self.conn.cursor()
    def fit(self):
        self.create_user()
    def query(self, query_string, value_dict=None):
        try:
            if value_dict != None:
                self.cur.execute(query_string, value_dict)
            else: 
                self.cur.execute(query_string)
            self.conn.commit()
            return self.cur
        except Exception as e:
            print('Error. Rollback connection')
            self.conn.rollback()
            print(e)
        return self.cur

    def create_user(self):
        create_query = """
        CREATE TABLE IF NOT EXISTS D_USER (
        DIM_SK SERIAL PRIMARY KEY,
        USER_NAME VARCHAR NOT NULL,
        PASSWORD VARCHAR NOT NULL
        );
        """
        self.query(create_query)
        print("Done create user table")
