import json
import secrets
from flask import Flask, request, jsonify
import methods
import authMethods
import mailSend
import client
from simpleUserData import user_data

app = Flask(__name__)


@app.route("/get-time-difference/<string:date>/<string:time>")
def get_time_difference(date, time):
    try:
        datetime_string = f"'{date}', '{time}'"
        print(f"Original datetime string: {datetime_string}")

        time_difference = client.send_time(datetime_string)
        # time_difference_string = str(time_difference)
        return f"{time_difference}", 200
    except:
        return "Invalid parameters", 400


@app.route("/token")
def get_token():
    # Generate a secure random token
    token = secrets.token_hex(16)  # You can adjust the length of the token as needed

    # You can do further processing or validation here if necessary

    # Return the token as a JSON response
    return token


@app.route("/Hello")
def get_hello_world():
    test = int(request.args.get('value1', 0))
    test2 = int(request.args.get('value2', 0))
    client.sendMessage()
    return "Hello world!" + str(test + test2), 200


@app.route("/get-user/users")
def get_user():
    return jsonify(user_data.get("users")), 200


@app.route("/get-user/<int:user_id>")
def get_user2(user_id):
    if methods.get_user_by_id(user_data, user_id):
        return jsonify(methods.get_user_by_id(user_data, user_id)), 200
    else:
        return "No", 200


@app.route("/create-food-data/<string:unique_user_token>/<string:user>", methods=["POST", "GET"])
def create_food_data(unique_user_token, user):
    data = request.get_json()

    json_object = json.loads(data)
    users = authMethods.load_Users()
    if user in users:
        if users[user][1] == unique_user_token:
            print(data)
            methods.save_to_file(json_object, unique_user_token)
            return jsonify(data), 201

    return jsonify({'error': 'Unauthorized access.'}), 400


@app.route("/getUserToken/<string:user>")
def get_user_token(user):
    users = authMethods.load_Users()

    if user in users:
        token = users[user][1]
        return token


@app.route("/signIn", methods=["POST", "GET"])
def signIn():
    data = request.get_json()
    json_object = json.loads(data)

    if 'username' not in json_object or 'password' not in json_object:
        return jsonify({'error': 'Username and password are required'}), 400

    username = json_object['username']
    password = json_object['password']
    token = secrets.token_hex(16)

    users = authMethods.load_Users()

    if username not in users:
        return jsonify({'authorized': False, 'error': 'Incorrect username or password1'}), 400

    if username in users:
        if users[username][0] == password:
            print(users[username])
            return jsonify({
                'authorized': True,
                'nickname': users[username][3],
                'height': users[username][4],
                'weight': users[username][5],
                'age': users[username][6],
                'message': 'Login successful!'}), 201

    return jsonify({'authorized': False, 'error': 'Incorrect username or password2'}), 400


@app.route('/register', methods=["POST", "GET"])
def register():
    data = request.get_json()
    json_object = json.loads(data)

    if 'username' not in json_object or 'password' not in json_object:
        return jsonify({'error': 'Username and password are required'}), 400

    username = json_object['username']
    password = json_object['password']
    token = json_object['token']
    confirmed_mail = False
    nickname = json_object['nickname']
    height = json_object['height']
    weight = json_object['weight']
    age = json_object['age']

    users = authMethods.load_Users()

    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    users[username] = password, token, confirmed_mail, nickname, height, weight, age
    print(users[username])
    authMethods.save_users(users)

    mailSend.sendMail(username, token)
    return jsonify({'message': 'User registered successfully, confirmation mail sent'}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
