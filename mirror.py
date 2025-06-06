import numpy as np
import matplotlib.pyplot as plt


def mirror(Xobj, Yobj, Xmirror, f, way):
    """Calculate the image from a mirror and draw the mirror."""
    Xdiff = Xmirror - Xobj
    Xdiffimg = (Xdiff * f) / (Xdiff - f)
    Ximg = Xmirror - Xdiffimg
    Yimg = -(Xdiffimg * Yobj) / Xdiff

    if way == 'L':
        way = 'R'
    else:
        way = 'L'

    angle = np.arange(2 * np.pi / 3, 4 * np.pi / 3, 0.001)
    R = Yobj * 1.5
    if f > 0:
        plt.plot(Xmirror - R + R * np.cos(angle + np.pi),
                 R * np.sin(angle + np.pi), 'b', linewidth=2)
    else:
        plt.plot(Xmirror + R + R * np.cos(angle),
                 R * np.sin(angle), 'b', linewidth=2)

    plt.plot([Xobj, Xmirror], [Yobj, 0], 'k--', linewidth=1)
    plt.plot([Xmirror, Ximg], [0, Yimg], 'k--', linewidth=1)
    plt.plot([Xobj, Xmirror], [Yobj, Yobj], 'k--', linewidth=1)
    plt.plot([Xmirror, Ximg], [Yobj, Yimg], 'k--', linewidth=1)
    return Ximg, Yimg, way
