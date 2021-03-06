import os
import psycopg2
from config import config
print("config: ", config)

conn = None
cur = None
def query(query_string, value_dict=None):
    conn = psycopg2.connect(database = config['POSTGRES_DATABASE'], 
                            user = config["POSTGRES_USER"], password = "password", host = "postgres", port = "5432")
    cur = conn.cursor()
    try:
        if value_dict != None:
            cur.execute(query_string, value_dict)
        else: 
            cur.execute(query_string)
        conn.commit()
        return cur
    except psycopg2.Error as t_err_msg:
        print('error: ', t_err_msg)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in transaction, reverting all changes using rollback ", error)
        conn.rollback()
    finally:
        print("PostgreSQL database connection is closed")
    return cur

import psycopg 

class PostgresSQL(object):
    def __init__(self, connection = f"""dbname={os.getenv("POSTGRES_DATABASE")} 
                 user={config["POSTGRES_USER"]} 
                 password={config["POSTGRES_PASSWORK"]} 
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
