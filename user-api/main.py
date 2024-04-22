from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to home page"


@app.route('/get-user/<user_id>')
def get_user(user_id):

    user_data = {
        'user_id' : user_id,
        'name' : 'Aqeel',
        'email' : 'aqeeladil@xyz.com'
    }
    
    extra = request.args.get('extra')         # /user-get/17?extra="hello world"
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200            # 200 is http status code for successfull request


@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)