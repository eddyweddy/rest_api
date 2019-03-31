# from flask import Flask
# import pytest
#
# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')
#
#
# def test_app_exists(self):
#     self.assertFalse(current_app is None)
#
#
#
# def test_app_is_testing(self):
#     self.assertTrue(current_app.config['TESTING'])
import flask_restful
from API.example.template import HelloWorld


def test_is_instance():
    instance = HelloWorld(flask_restful.Resource)
    assert isinstance(instance)