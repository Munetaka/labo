from flask import Flask, jsonify, request, abort

api = Flask(__name__)

test_list = [
    {
        'id': 1,
        'desc': 'no.1'
    },
    {
        'id': 2,
        'desc': 'no.2'
    }
]

@api.route('/')
def index():
    return 'restful api test !'

@api.route('/test/get', methods=['GET'])
def test_get():
    return jsonify({'test_list': test_list})

@api.route('/test/get/<int:id>', methods=['GET'])
def test_get_key(id):
    test = [test for test in test_list if test['id'] == id]
    if len(test) == 0:
        abort(404)
    return jsonify({'test': test[0]})

@api.route('/test/post', methods=['POST'])
def test_post():
    if not request.json or not 'desc' in request.json:
        abort(400)
    test_id = test_list[-1]['id'] + 1
    test = {
        'id': test_id,
        'desc': request.json['desc']
    }
    test_list.append(test)
    return jsonify({'test_list': test_list}), 201

@api.route('/test/delete/<int:id>', methods=['DELETE'])
def test_delete(id):
    test = [test for test in test_list if test['id'] == id]
    if len(test) == 0:
        abort(404)
    test_list.remove(test[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    api.run(debug=True)
