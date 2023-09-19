import unittest
import jsonapi

class TestCustomJSON(unittest.TestCase):
    def test_custom_encoder_complex(self):
        obj = complex(3.0, 4.0)
        encoded = jsonapi.dumps(obj)
        self.assertEqual(encoded, '{"complex": true, "real": 3.0, "imag": 4.0}')

    def test_custom_encoder_range(self):
        obj = range(1, 5, 2)
        encoded = jsonapi.dumps(obj)
        self.assertEqual(encoded, '{"range": true, "start": 1, "stop": 5, "step": 2}')

    def test_dumps(self):
        obj = {"name": "John", "age": 30}
        encoded = jsonapi.dumps(obj)
        self.assertEqual(encoded, '{"name": "John", "age": 30}')

    def test_loads(self):
        json_str = '{"name": "Alice", "age": 25}'
        decoded = jsonapi.loads(json_str)
        self.assertEqual(decoded, {"name": "Alice", "age": 25})

if __name__ == '__main__':
    unittest.main()