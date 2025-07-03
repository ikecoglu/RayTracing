import os
import sys
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plane_mirror import plane_mirror


def test_plane_mirror_basic():
    x_img, y_img, way = plane_mirror(5, 2, 10, 'L')
    assert x_img == 15
    assert y_img == 2
    assert way == 'R'
