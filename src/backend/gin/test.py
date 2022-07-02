import psycopg

conn = psycopg.connect(dbname = "postgres", user = "user", password = "pass", host = "0.0.0.0", port = "5432")
cur = conn.cursor()
