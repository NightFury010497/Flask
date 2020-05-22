from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/home/', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

if __name__ == '__main__':
    app.run(debug=True)