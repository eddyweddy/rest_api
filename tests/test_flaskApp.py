from flask import Flask
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')


def test_app_exists(self):
    self.assertFalse(current_app is None)



def test_app_is_testing(self):
    self.assertTrue(current_app.config['TESTING'])
