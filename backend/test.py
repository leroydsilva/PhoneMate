import unittest
from app import create_app
from config import TestConfig
from mysql import mysql

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():
            mysql.init_app(self.app)

    def test_phone(self):
        phone_response=self.client.get('/phone/Phone/45')   

        self.assertEquals(phone_response.status_code, 200)     

    def test_phone_POST(self):
        phone_response=self.client.post('/phone/Phone',
        json={
            "Phone_id":2,
            "Phone_name": "realme 41",
            "Phone_price": 4500
        })    
        json_data=phone_response.json
        self.assertEquals(json_data, {"message":"realme 41"})

    def teardown(self):
        with self.app.app_context():
            mysql.session.remove()

if __name__ == "__main__":
    unittest.main()