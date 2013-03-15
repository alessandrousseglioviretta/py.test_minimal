import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from calc import *


def test_plus():
    assert plus(1, 2) == 3


def test_minus():
    assert minus(3, 2) == 1


def test_times():
    assert times(2, 3) == 6

#  change 10
