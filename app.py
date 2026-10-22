from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from auth import check_pass
import json

front = Flask(__name__)
CORS(front)

@front.route('/', methods=['GET'])
@front.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@front.route('/signup', methods=['GET'])
def signup_page():
    # Skip signup page and redirect straight to login
    return redirect(url_for('login_page'))

@front.route('/login', methods=['POST'])
@front.route('/sign_up', methods=['POST'])
def login():
    login_data = request.get_json() or {}
    username = login_data.get('username')
    password = login_data.get('password')

    if not username or not password:
        return jsonify({
            "status": "error",
            "message": "Username and password are required!"
        }), 400

    try:
        status = check_pass(username, password)
        if status:
            print(f"login by {username} is done.")
            return jsonify({
                "status": "sucess",
                "message": f"{username} login sucessful :)."
                
            }), 200
        
        elif status is False:
            return jsonify({
                "status": "error",
                "message": "Invalid username or password!"
            }), 401
        elif status==10:
            return jsonify({
                "status":"error",
                "message":"User not found :("
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Database connection error! Please verify database status."
            }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Server error, please try again."
        }), 500

if __name__ == "__main__":
    front.run(debug=True)