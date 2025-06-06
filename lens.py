import numpy as np
import matplotlib.pyplot as plt


def lens(Xobj, Yobj, Xlens, f, way, draw_lens):
    """Calculate the image from a thin lens and optionally draw the lens."""
    if way == 'L':
        Xdiff = Xlens - Xobj
        Xdiffimg = (Xdiff * f) / (Xdiff - f)
        Ximg = Xlens + Xdiffimg
        Yimg = -(Xdiffimg * Yobj) / Xdiff
    else:
        Xdiff = Xobj - Xlens
        Xdiffimg = (Xdiff * f) / (Xdiff - f)
        Ximg = Xlens - Xdiffimg
        Yimg = -(Xdiffimg * Yobj) / Xdiff

    if draw_lens == 1:
        angle = np.arange(2 * np.pi / 3, 4 * np.pi / 3, 0.001)
        R = Yobj * 1.5
        if f > 0:
            plt.plot(Xlens + R / 2 + R * np.cos(angle), R * np.sin(angle), 'b', linewidth=2)
            plt.plot(Xlens - R / 2 + R * np.cos(angle + np.pi),
                     R * np.sin(angle + np.pi), 'b', linewidth=2)
        else:
            plt.plot(Xlens - R + R * np.cos(angle + np.pi),
                     R * np.sin(angle + np.pi), 'b', linewidth=2)
            plt.plot(Xlens + R + R * np.cos(angle),
                     R * np.sin(angle), 'b', linewidth=2)

    plt.plot([Xobj, Ximg], [Yobj, Yimg], 'k--', linewidth=1)
    plt.plot([Xobj, Xlens], [Yobj, Yobj], 'k--', linewidth=1)
    plt.plot([Xlens, Ximg], [Yobj, Yimg], 'k--', linewidth=1)
    return Ximg, Yimg
