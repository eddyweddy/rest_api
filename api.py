from flask import Flask
from flask_restful import Resource, Api

# Initial HelloWorld to verify Docker build
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Docker': 'hello world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
