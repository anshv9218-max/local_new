from flask import Flask ,request ,jsonify,render_template
from flask_cors import CORS
from auth import getpass ,verify_register
import json
front=Flask(__name__)
CORS(front)
@front.route('/sign_up',methods=['POST'])
def sign_up():
    login=request.get_json()#collecting data from frontend and converting from json to dic.
    username=login.get('username')#username from dict
    password=login.get('password')#password from dict
    try:
        status=verify_register(username,password)
        if status:
            return jsonify({
                "status":"sucess",
                "message":f"{username} login sucessful."
            }),200
        else:
            return jsonify({
                "status":"error!! username already exist "
            }),401
    except Exception as e:
        return jsonify({"status": "error", "message": "Server error, please try again."}), 500
@front.route('/signup',methods=['GET'])
def signup_page():
    return render_template('signup.html')

if __name__ == "__main__":
    front.run(debug=True)  