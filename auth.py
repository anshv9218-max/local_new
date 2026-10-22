from db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash 
import psycopg2
from datetime import datetime
# convert normal password to hashed password
def hash_pass(password):
    return generate_password_hash(password)


# insert user (signup function)
def insert_user(username, password):
    con = None
    try:
        con=get_db_connection()
        # print(con)

        if con is None:
            return False
        cursor = con.cursor()
        hash_password = hash_pass(password)
        query="INSERT into login_info (username,password) values (%s,%s);"
        cursor.execute(query,(username,hash_password))
        con.commit()
        print("user created sucessfully !!")
        return True
    except Exception as e:
        
        print(f"Database error occurred: {e}")
        return False
# fetch data from login_info table
def get_user():
    con=get_db_connection()
    if con is None:
        return False
    try:
        cursor=con.cursor()
        query="Select * from login_info;"
        cursor.execute(query)
        value=cursor.fetchall()
        print(value)
    except Exception as e:
        print(f"database error occured!{e}")

def check_pass(username,password):
    con=get_db_connection()
    if con is None:
        return False
    try:
        cursor=con.cursor()
        query="Select password from login_info where username=(%s);"
        cursor.execute(query,(username,))
        value=cursor.fetchone()
        if value is None:
            print("user not found !!")
            return 10
        true_pass=check_password_hash(value[0],password)

        if true_pass:
            time=datetime.now()
            file=open("login.txt","+a")
            file.write(f"login by {username} , {password} is done on {time} \n")
            file.close()
            print("login successfull !!")
            return True
            
        else:
            print("not matched !!") 
            return False
             
    except Exception as e:
        print(f"Something went wrong :( {e}") 
        return False

     


# username=input("unsername: ")
# password=input("password: ")
# insert_user(username,password)
# get_user()
# check_pass(username,password)

