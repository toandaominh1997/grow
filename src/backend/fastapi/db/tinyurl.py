from .utils import query
import psycopg2


class TinyURLDB(object):
    def __init__(self):
        conn = psycopg2.connect(database = "database", user = "user", password = "password", host = "postgres", port = "5432")
        self.cur = conn.cursor()
        self.conn = conn
    def query(self, query_string, value_dict = None):
        try:
            if value_dict != None:
                self.cur.execute(query_string, value_dict)
            else: 
                self.cur.execute(query_string)
            return self.cur
        except psycopg2.Error as t_err_msg:
            print('error: ', t_err_msg)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error in transaction, reverting all changes using rollback ", error)
            self.conn.rollback()
        finally:
            print("PostgreSQL database connection is closed")
        return self.cur

    def fit(self):
        self.create_tinyurl()
    def create_tinyurl(self):
        query_string = """
        CREATE TABLE IF NOT EXISTS D_TINYURL (
        id SERIAL PRIMARY KEY,
        alias VARCHAR,
        long_url VARCHAR NOT NULL,
        domain VARCHAR NOT NULL,
        UNIQUE(alias)
        );
        """

        query(query_string)
        print('done create D_TINYURL')
        return True


    def insert_tinyurl(self, alias, long_url, domain = None):
        q = f""" 
        INSERT INTO D_TINYURL(alias, long_url, domain)
        VALUES
        (%(alias)s, %(long_url)s, %(domain)s)
        """
        values = {"alias": alias,
                  "long_url": long_url,
                  "domain": domain,
                  }
        query(q, values)
        return True

    def validate_longurl(self, tiny_url, long_url):
        q = f""" 
        SELECT
        distinct
        alias,
        long_url
        FROM D_TINYURL
        where 1=1
        and long_url = '{long_url}'
        """
        self.cur.execute(q)
        output = self.cur.fetchall()
        print('output', output)
        if len(output) > 0:
            return output
        return None

    def validate_alias_longurl(self, alias, long_url):
        q = f""" 
        SELECT
        distinct
        domain,
        alias
        FROM D_TINYURL
        where 1=1
        and alias = '{alias}'
        and long_url = '{long_url}'
        """
        self.cur.execute(q)
        output = self.cur.fetchall()
        print('output alias long url', output)
        if len(output) > 0:
            return output
        return None
    def get_alias(self, alias):
        q = f""" 
        SELECT
        distinct
        long_url
        FROM D_TINYURL
        where 1=1
        and alias = '{alias}'
        """
        self.cur.execute(q)
        output = self.cur.fetchall()
        if len(output) > 0:
            return output
        return None
    def validate_alias(self, alias):
        q = f""" 
        SELECT
        distinct
        domain,
        alias
        FROM D_TINYURL
        where 1=1
        and alias = '{alias}'
        """
        self.cur.execute(q)
        output = self.cur.fetchall()
        print('output', output)
        if len(output) > 0:
            return output
        return None
    def get_db(self):
        q = f""" 
        SELECT
        distinct
        *
        FROM D_TINYURL
        where 1=1
        """
        self.cur.execute(q)
        output = self.cur.fetchall()
        if len(output) > 0:
            return output
        return None
