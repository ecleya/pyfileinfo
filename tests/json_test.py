import os
import unittest

from pyfile import pyfile, Json
from tests import DATA_ROOT


class TestJson(unittest.TestCase):
    def test_dict_json_file(self):
        file = pyfile(os.path.join(DATA_ROOT, 'dict.json'))
        self.assertTrue(isinstance(file, dict))
        self.assertTrue(isinstance(file, Json))

    def test_list_json_file(self):
        file = pyfile(os.path.join(DATA_ROOT, 'list.json'))
        self.assertTrue(isinstance(file, list))
        self.assertTrue(isinstance(file, Json))

    def test_dict_json_access(self):
        file = pyfile(os.path.join(DATA_ROOT, 'dict.json'))
        self.assertEqual(file['a'], 1)

    def test_list_json_access(self):
        file = pyfile(os.path.join(DATA_ROOT, 'list.json'))
        self.assertEqual(file[0], {"a": 1, "b": 2})