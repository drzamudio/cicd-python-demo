import unittest
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)
        self.assertEqual(app.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(app.subtract(5, 2), 3)
        self.assertEqual(app.subtract(0, 3), -3)

if __name__ == "__main__":
    unittest.main()
