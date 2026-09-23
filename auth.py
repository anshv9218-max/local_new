from db import get_db_connection
from werkzeug.security import generate_password_hash,check_password_hash 
import psycopg2
def getpass(password):
    return generate_password_hash(password)
def verify_register(username,password):
    con=get_db_connection()
    cursor=con.cursor()
    try:
        query="select password from login_person where username=%s;"
        cursor.execute(query,(username,))
        result=cursor.fetchone()
        cursor.close()
        con.close()
        if result is not None:
            db_pass=result[0]
            if check_password_hash(db_pass,password)==True:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print("Error in Database !")
        return None
def insert_user(username,password):
    con=get_db_connection()
    cursor=con.cursor()
    hash_pass=getpass(password)
    try:
        query="insert into login_person (username,password) values(%s,%s);"
        cursor.execute(query,(username,hash_pass,))
        con.commit()
        cursor.close()
        con.close()
        return True
    
    except Exception as e:
        if con:
            con.rollback()
        print("Database error occured!!")
        return False


