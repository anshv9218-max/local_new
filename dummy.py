from db import  get_db_connection
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash 
# from auth import getpass
def insert_user(username, password):
    con = None
    try:
        con=get_db_connection()
        # print(con)

        if con is None:
            return False
        cursor = con.cursor()
        hash_password = generate_password_hash(password)
        query="INSERT into login_info (username,password) values (%s,%s);"
        cursor.execute(query,(username,hash_password))
        con.commit()
        print("user created sucessfully !!")
        return True
    except Exception as e:
        
        print(f"Database error occurred: {e}")
        return False


userf=open("username.txt","r",encoding="utf-8")
passf=open("password.txt","r",encoding="utf-8")
x=1
for username,password in zip(userf,passf):
    username=username.strip()
    password=password.strip()
    insert_user(username,password)
    print(x)
    x=x+1
userf.close()
passf.close()


