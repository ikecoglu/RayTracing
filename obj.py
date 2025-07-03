import matplotlib.pyplot as plt


def obj(Xobj, y):
    """Draw an object in the scene.

    Parameters
    ----------
    Xobj : float
        Position along the X axis.
    y : float
        Height of the object.
    """
    plt.plot([Xobj, Xobj], [0, y], 'r', linewidth=2)
    return Xobj, y
