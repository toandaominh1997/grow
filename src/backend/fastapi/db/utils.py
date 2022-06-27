import psycopg2
conn = None
cur = None
def query(query_string, value_dict=None):
    conn = psycopg2.connect(database = "database", user = "user", password = "password", host = "postgres", port = "5432")
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
