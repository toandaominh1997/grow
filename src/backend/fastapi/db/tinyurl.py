from .utils import query, PostgresSQL
import psycopg2


class TinyURLDB(object):
    def __init__(self):
        self.pg = PostgresSQL()
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

        self.pg.query(query_string)
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
        self.pg.query(q, values)
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

        cur = self.pg.query(q)
        output = cur.fetchall()
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
        cur = self.pg.query(q)
        output = cur.fetchall()
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
        cur = self.pg.query(q)
        output = cur.fetchall()
        if len(output) > 0:
            return output
        return None
    def validate_alias(self, alias):
        q = f""" 
        SELECT
        distinct
        domain,
        alias,
        long_url
        FROM D_TINYURL
        where 1=1
        and alias = '{alias}'
        """
        cur = self.pg.query(q)
        output = cur.fetchone()
        print('output', output)
        print("check fetchone", cur.fetchone())
        return output
    def get_db(self):
        q = f""" 
        SELECT
        distinct
        *
        FROM D_TINYURL
        where 1=1
        """
        cur = self.pg.query(q)
        output = cur.fetchall()
        if len(output) > 0:
            return output
        return None
    def delete_db(self):
        query_string = """ 
DROP TABLE IF EXISTS D_TINYURL;
        """
        self.pg.query(query_string)
