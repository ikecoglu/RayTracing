import matplotlib.pyplot as plt


def image_plane(Ximg, Yimg):
    """Draw the image plane.

    Parameters
    ----------
    Ximg, Yimg : float
        Coordinates of the image point.
    """
    plt.plot([Ximg, Ximg], [0, Yimg], 'g', linewidth=2)
