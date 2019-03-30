from flask import Flask
from flask_restful import Api
from API.helloWorld import helloWorld

app = Flask(__name__)

api = Api(app)

api.add_resource(helloWorld.helloWorld, "/api/helloWorld")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
