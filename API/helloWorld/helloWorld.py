from flask import Flask
from flask_restful import Resource, Api

# helloworld responses


class helloWorld(Resource):
    def get(self):
        return {'Docker': 'hello world'}

    def post(self):
        return{'Docker': 'hello world post'}



