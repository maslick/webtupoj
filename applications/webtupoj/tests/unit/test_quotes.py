import unittest

from applications.webtupoj.controllers.default import quotes


class TestQuotes(unittest.TestCase):
    def test_quotes_route(self):
        res = quotes()
        self.assertEqual(5, len(res["citations"]))


if __name__ == '__main__':
    unittest.main()
