import unittest

from HTMLTestRunner.runner import HTMLTestRunner
from Unit_Test import TestCase


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
        my_test_runnner = HTMLTestRunner(
            output = "report",
            title = "Test report",
            report_name = "report",
            tested_by = "Lazarica Petrut"
        )

        my_test_runnner.run(my_test_suit)
