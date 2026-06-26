import unittest

class TestInsuranceESG(unittest.TestCase):

    def test_esg_score(self):
        score = 82
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

if __name__ == "__main__":
    unittest.main()