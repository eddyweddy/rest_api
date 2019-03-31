from flask import Flask
from flask_restful import Api
import API.example.template


app = Flask(__name__)

api = Api(app)

api.add_resource(API.example.template.HelloWorld, '/')
api.add_resource(API.example.template.GitStatus, '/status')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
