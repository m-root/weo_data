import unittest
from flask import json
from flask.testing import FlaskClient

from main import app


class FlaskTest(unittest.TestCase):

    app: FlaskClient

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        data = json.load(open('../data/test_data.json', 'r'))

        response = self.app.post('/predict', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
