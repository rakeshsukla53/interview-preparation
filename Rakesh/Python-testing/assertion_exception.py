__author__ = 'rakesh'

import pytest

def test_comparison():

    set1 = set('1308')
    set2 = set('8035')
    print set1, set2
    assert set1 == set2


# Special comparisons are done for a number of cases:
#
#     comparing long strings: a context diff is shown
#     comparing long sequences: first failing indices
#     comparing dicts: different entries


