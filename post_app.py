import flask

from flask import Flask, jsonify, request

app = flask.Flask(__name__)

users = [
    {'id': 1, 'name': 'yahye'},
    {'id': 2, 'name': 'mohamed'},
    {'id': 3, 'name': 'axmed'}
]


@app.route('/')
def home(): return ({
    'name': "yahye farah"
})


# @app.route('/users')
# def getUser():
#     return jsonify(users)


@app.route('/users', methods=['GET'])
def getUser():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def adduser():
    data = request.get_json()

    newUser = {
        'id': len(users) + 1,
        'name': data['name']
    }

    users.append(newUser)
    return jsonify(newUser), 201


@app.route('/users/<int:get_one>', methods=['GET'])
def getOneUser(get_one):
    for user in users:
        if user['id'] == get_one:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/users/<int:updateName>' ,  methods=['PUT'])
def UpdateName(updateName):
    data = request.get_json()
    for user in users:
        if user['id'] == updateName:
            user['name'] = data.get(
                'name', user['name']
            )
        return jsonify(user)
    return jsonify({
        'message': 'unfound '
    }), 404




@app.route('/users/<int:deleteone>' , methods=['DELETE'])
def deleteONe(deleteone):
    for user in users:
        if user['id'] == deleteone:
            users.remove(user)
            return jsonify({"message": "User deleted"})
    return jsonify({"message": 'no found'} , 404)





if __name__ == '__main__':
    app.run(debug=True)
