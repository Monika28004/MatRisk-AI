import unittest

class TestFinancialRisk(unittest.TestCase):

    def test_risk_level(self):
        risk = "HIGH"
        self.assertIn(risk, ["LOW", "MEDIUM", "HIGH"])

if __name__ == "__main__":
    unittest.main()