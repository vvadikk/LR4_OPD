import unittest
from app import app
class InputTests(unittest.TestCase):
    def test_angle(self):
        tester = app.test_client(self)
        response = tester.post('/', data={'f': 'sin', 'x': 'i', 'e': '5', 'degOrRad': 'deg'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Argument must be a number', response.data)
    def test_measurement(self):
        tester = app.test_client(self)
        response = tester.post('/', data={'f': 'sin', 'x': '10', 'e': '5', 'degOrRad': 'i'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Choose: deg or rad', response.data)
    def test_function(self):
        tester = app.test_client(self)
        response = tester.post('/', data={'f': 'i', 'x': '10', 'e': '5', 'degOrRad': 'deg'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No such function', response.data)
    def test_precision(self):
        tester = app.test_client(self)
        response = tester.post('/', data={'f': 'sin', 'x': '10', 'e': 'i', 'degOrRad': 'deg'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Precision must be a number', response.data)
if __name__ == '__main__':
    unittest.main()
