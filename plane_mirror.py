import matplotlib.pyplot as plt


def plane_mirror(Xobj, Yobj, Xmirror, way):
    """Reflects the ray from a flat mirror and returns the virtual image.

    Parameters
    ----------
    Xobj, Yobj : float
        Object location.
    Xmirror : float
        Position of the mirror along the X axis.
    way : {'L', 'R'}
        Direction of propagation before reflection.

    Returns
    -------
    tuple
        (Ximg, Yimg, way) - coordinates of the virtual image and new
        propagation direction.
    """
    Ximg = 2 * Xmirror - Xobj
    Yimg = Yobj

    plt.plot([Xmirror, Xmirror], [0, Yobj * 1.5], 'b', linewidth=2)
    plt.plot([Xobj, Xmirror], [Yobj, Yobj], 'k--', linewidth=1)
    plt.plot([Xmirror, Ximg], [Yobj, Yimg], 'k--', linewidth=1)

    way = 'R' if way == 'L' else 'L'
    return Ximg, Yimg, way
