import unittest
import yaml


class TestData(unittest.TestCase):
    def setUp(self):
        data_files = [
            'url',
            'publications',
        ]

        self.data = {}
        for data_current in data_files:
            with open('_data/{}.yml'.format(data_current)) as f:
                self.data[data_current] = yaml.load(f)

    def test_parse_yaml(self):
        pass

    def test_url_exist(self):
        self.assertEqual(len(self.data['url'].items()),3)

    def test_at_least_5_pubs(self):
        for id_author, pubs in self.data['publications'].items():
            self.assertGreater(len(pubs), 5)
