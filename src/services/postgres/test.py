import psycopg2

conn = psycopg2.connect(database = "database", user = "postgres", password = "mysecretpassword", host = "0.0.0.0", port = "5432")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')

conn.commit()
conn.close()
