
from flask_restful import Resource
from flask import jsonify
import git

# helloworld responses


class HelloWorld(Resource):
    def get(self):
        return {'Docker': 'hello world'}

    def post(self):
        return{'Docker': 'hello world post'}


class GitStatus(Resource):
    def get(self):
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        return jsonify(description="plain text",lastcommitsha=sha)