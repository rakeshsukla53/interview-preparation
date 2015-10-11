__author__ = 'rakesh'

import unittest

class TestCase(unittest.TestCase):

    def one_plus_one(self):
        assert 1 + 1 == 2

    def not_two(self):
        assert not 2 == 2


