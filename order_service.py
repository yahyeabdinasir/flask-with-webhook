from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 1, "item": "Laptop"},
    {"id": 2, "item": "Phone"}
]


@app.route('/orders', methods=['GET'])
def get_users():
    return jsonify(orders)


if __name__ == "__main__":
    app.run(port=5004)
