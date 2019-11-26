import unittest

from applications.webtupoj.controllers.default import index


class TestIndex(unittest.TestCase):
    def test_index_route(self):
        res = index()
        self.assertTrue('BACKEND_URL=ya.ru', res['message'])


if __name__ == '__main__':
    unittest.main()
