import matplotlib.pyplot as plt


def obj(Xobj, y):
    """Draws the object as a vertical red line."""
    plt.plot([Xobj, Xobj], [0, y], 'r', linewidth=2)
    return Xobj, y
