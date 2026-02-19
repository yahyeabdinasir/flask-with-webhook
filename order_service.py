import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"id": 1, "item": "Laptop"},
    {"id": 2, "item": "Phone"}
]


@app.route('/orders')
def getorders():
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def createOrder():
    data = request.getjson()
    orders.append(data)

    requests.post(
        'http://127.0.0.1:5003/webhook/order-created' , json=data
    )

    return jsonify(data),201


if __name__ == "__main__":
    app.run(port=5004)
