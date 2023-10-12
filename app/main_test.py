import unittest
from main import app, get_mode, backwards_string
import os

class SimpleCITest(unittest.TestCase):

    def test_setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_backwards_string(self):
       random_string = "this is my test string"
       random_string_reversed = "gnirts tset ym si siht"
       self.assertEqual(random_string_reversed, backwards_string(random_string))

    def test_get_env(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())

if __name__ == '__main__':
    unittest.main()