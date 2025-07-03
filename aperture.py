import matplotlib.pyplot as plt


def aperture(Xaperture, size):
    """Draw a simple aperture.

    Parameters
    ----------
    Xaperture : float
        Position of the aperture along the X axis.
    size : float
        Total height of the aperture opening.
    """
    half = size / 2.0
    plt.plot([Xaperture, Xaperture], [-half, half], 'm', linewidth=2)
