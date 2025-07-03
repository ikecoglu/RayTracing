import os
import sys
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lens import lens


def test_lens_basic():
    x_img, y_img = lens(0, 1, 10, 5, 'L', 0)
    assert x_img == 20.0
    assert y_img == -1.0
