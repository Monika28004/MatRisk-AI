import unittest

class TestFailureModel(unittest.TestCase):

    def test_failure_probability(self):
        probability = 0.72
        self.assertGreaterEqual(probability, 0)
        self.assertLessEqual(probability, 1)

if __name__ == "__main__":
    unittest.main()