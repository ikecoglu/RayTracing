import matplotlib.pyplot as plt


def image_plane(Ximg, Yimg):
    """Draw the image plane as a vertical green line."""
    plt.plot([Ximg, Ximg], [0, Yimg], 'g', linewidth=2)
