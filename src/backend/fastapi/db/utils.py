import psycopg2
conn = psycopg2.connect(database = "postgres", user = "user", password = "password", host = "0.0.0.0", port = "5432")
cur = conn.cursor()
def query(query_string, value_dict=None):
    try:
        if value_dict != None:
            cur.execute(query_string, value_dict)
        else: 
            cur.execute(query_string)
        conn.commit()
        return cur
    except Exception as e:
        print('Error. Rollback connection')
        conn.rollback()
        print(e)
    return cur
