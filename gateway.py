from flask import  Flask ,jsonify
import requests

app = Flask(__name__)


usersService = "http://127.0.0.1:5004"
userOrders = "http://127.0.0.1:5004"

@app.route('/users')
def GrtUserService():
    response = requests.get(f'{usersService}/users')
    return  jsonify(response.json())


@app.route('/orders')
def GetUserOrders():
    response = requests.get(f'{userOrders}/users')
    return  jsonify(response.json())



if __name__ == '__main':
    app.run(port=5000)
