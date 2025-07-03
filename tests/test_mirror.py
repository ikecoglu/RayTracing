import os
import sys
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mirror import mirror


def test_mirror_basic():
    x_img, y_img, way = mirror(0, 1, 10, 5, 'L')
    assert x_img == 0.0
    assert y_img == -1.0
    assert way == 'R'


def test_mirror_right_side():
    x_img, y_img, way = mirror(20, 1, 10, 5, 'R')
    assert way == 'L'
    assert y_img == -1.0
    assert x_img == 20.0
