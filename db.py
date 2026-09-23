import psycopg2
def get_db_connection():
    try:
        connect=psycopg2.connect(
            host="localhost",
            database="login",
            user="postgres",
            password="9218ansh",
            port="5432"
        )
        return connect
    except Exception as error:
        print("DATABASE failure occurs")
        return None
    