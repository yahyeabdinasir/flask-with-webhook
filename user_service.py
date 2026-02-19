from flask import Flask, jsonify , request


app = Flask(__name__)

users = [
    {"id": 1, "name": "yahye"},
    {"id": 2, "name": "mohamed"}
]




@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/webhook/order-created' , methods=['POST'])
def orderWebhook():
    data = request.get_json()
    print("webhook recieved " , data)
    return  jsonify({
        'messeage'  : 'webhook received'
    })

if __name__ == "__main__":
    app.run(port=5003)
