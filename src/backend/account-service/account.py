import psycopg2
conn = psycopg2.connect(database = "postgres", user = "user", password = "grows1234", host = "0.0.0.0", port = "5432")
cur = conn.cursor()

create_query = """
CREATE TABLE IF NOT EXISTS ACCOUNTS (
    user_id serial PRIMARY KEY,
    username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL
);
"""
update_query = """
INSERT INTO ACCOUNTS (user_id, username, password) VALUES (DEFAULT, %s, %s)
"""

get_query = """
SELECT 
user_id,
username,
password
FROM ACCOUNTS
WHERE username='{username}'
"""

auth_query = """
SELECT 
user_id,
username,
password
FROM ACCOUNTS
WHERE username='{username}'
password='{password}'
"""

show_query = """
SELECT
*
FROM ACCOUNTS
"""
def create_table():
    cur.execute(create_query)
create_table()

def update_table(username, password):
    cur.execute(update_query, (username, password))

update_table("testne", "1234")
# update_table("toan", "1234")
# update_table("kaka", "1234")

def get_username(username):
    cur.execute(get_query.format(username = username))
    print(cur.fetchone())
def check_username(username):
    cur.execute(get_query.format(username = username))
    if cur.fetchone() is None:
        return False
    return True
def check_auth(username, password):
    cur.execute(auth_query.format(username = username, password = password))
    if cur.fetchone() is None:
        return False
    return True
def show_table():
    cur.execute(show_query)
    print('show table')
    print(cur.fetchall())

# get_username('toan')
# show_table()



