import psycopg2

def get_db_connection():
    try:
        connect = psycopg2.connect(
            host="127.0.0.1",
            database="login",
            user="postgres",
            password="9218ansh",
            port="5432",
            connect_timeout=1
        )
        # print("connected successfully")
        return connect
    except Exception as error:
        print("PostgreSQL connection failed")
        return None
