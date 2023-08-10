import unittest

from HTMLTestRunner.runner import HTMLTestRunner
from Unit_Tests import TestCase


# Test Suit Class
class TestingClass(unittest.TestCase):

    # Test Suit for all the other tests
    def test_suit(self):
        my_test_suit = unittest.TestSuite()
        my_test_suit.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase),
            #unittest.defaultTestLoader.loadTestsFromTestCase(TestCase2)#,
            #unittest.defaultTestLoader.loadTestsFromTestCase(EasyTest)
        ])

        # Test Runner HTML Report
        my_test_runner = HTMLTestRunner(
            output = "report",
            title = "Test report",
            report_name = "report",
            tested_by = "Lazarica Petrut"
        )

        my_test_runner.run(my_test_suit)

if __name__ == "__main__":
    unittest.main()