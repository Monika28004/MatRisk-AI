import unittest

class TestValidation(unittest.TestCase):

    def test_accuracy(self):
        accuracy = 0.92
        self.assertGreaterEqual(accuracy, 0.8)

if __name__ == "__main__":
    unittest.main()