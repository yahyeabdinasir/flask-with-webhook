import flask
from flask import Flask, jsonify

app = flask.Flask(__name__)

users = [
    {'id': 1, 'name': 'yahye'},
    {'id': 2, 'name': 'mohamed '}
]
@app.route("/")
def index():
    return jsonify({
        'messege': 'User Api',

    })


@app.route('/users')
def getUsers():
    return jsonify(users)

@app.route('/users/<int:user_id>/')
def getUser(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
