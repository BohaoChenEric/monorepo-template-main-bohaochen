import json
import unittest
from jsonapi import custom_dumps, custom_loads

class TestCustomJSONEncodingDecoding(unittest.TestCase):
    def test_complex_encoding_decoding(self):
        # Test encoding and decoding of complex numbers
        complex_number = complex(2.5, 3.0)
        encoded = custom_dumps(complex_number)
        decoded = custom_loads(encoded)
        self.assertEqual(complex_number, decoded)

    def test_range_encoding_decoding(self):
        # Test encoding and decoding of range objects
        my_range = range(1, 10, 2)
        encoded = custom_dumps(my_range)
        decoded = custom_loads(encoded)
        self.assertEqual(list(my_range), list(decoded))

if __name__ == '__main__':
    unittest.main()
