from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "yahye"},
    {"id": 2, "name": "mohamed"}
]




@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(port=5003)
