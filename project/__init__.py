from flask import Flask


def create_api(config_filename=None):
    api = Flask(__name__, instance_relative_config=True)
    api.config.from_pyfile(config_filename)
    get_api(api)
    return api


def get_api(api):
    # import each api here
    from project import helloWorld

    # Add a new registration for each API that you are creating
    api.register_blueprint(helloWorld)
