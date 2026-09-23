from db import  get_db_connection
import psycopg2
from auth import getpass
def insert_user(username,password):
    con=get_db_connection()
    cursor=con.cursor()
    hash_pass=getpass(password)
    try:
        query="insert into login_person (username,password) values(%s,%s);"
        cursor.execute(query,(username,hash_pass))
        con.commit()
        cursor.close()
        con.close()
        return True
    
    except Exception as e:
        if con:
            con.rollback()
        print("Database error occured!!")
        return False


insert_user("prateek@gmail.com","9218Prateek")
