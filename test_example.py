import unittest
from example import hello_world

class TestHello(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, GitHub Actions! 2")

if __name__ == "__main__":
    unittest.main()