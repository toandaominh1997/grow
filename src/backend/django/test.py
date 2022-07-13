import os
from config import config
import psycopg 

print("Config: ", config)

class PostgresSQL(object):
    def __init__(self, connection = f"""dbname={config["POSTGRES_DATABASE"]} 
                 user={config["POSTGRES_USER"]} 
                 password={config["POSTGRES_PASSWORD"]} 
                 host={config["POSTGRES_HOST"]} 
                 port={config["POSTGRES_PORT"]}
                 """):
        print("connection: ", connection)
        self.conn = psycopg.connect(connection)
    def query(self, query_string, params = None):
        try:
            cur = self.conn.execute(query = query_string, params = params)
            return cur
        except BaseException or psycopg.Error as e:
            print('Error: ', e)
            self.conn.rollback()
        finally:
            print('commit')
            self.conn.commit()
        return None
db = PostgresSQL()

query = """ 
SELECT *
FROM pg_catalog.pg_tables
"""
db.query(query)
