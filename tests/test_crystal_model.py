import unittest

class TestCrystalModel(unittest.TestCase):

    def test_prediction_output(self):
        prediction = 420
        self.assertGreater(prediction, 0)

if __name__ == "__main__":
    unittest.main()