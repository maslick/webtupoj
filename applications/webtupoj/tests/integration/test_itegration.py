import unittest

from gluon.contrib.webclient import WebClient

client = WebClient('http://127.0.0.1:8080/', postbacks=True)


class IntegrationTest(unittest.TestCase):
    def test_index(self):
        client.get('index')
        assert 200 == client.response.status


if __name__ == '__main__':
    unittest.main()
