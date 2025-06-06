import matplotlib.pyplot as plt

from obj import obj
from lens import lens
from mirror import mirror
from image_plane import image_plane


def main():
    plt.figure()

    way = 'L'
    Xobj, Yobj = obj(15, 1)

    Ximg, Yimg = lens(Xobj, Yobj, 30, -10, way, 1)
    image_plane(Ximg, Yimg)

    Ximg, Yimg, way = mirror(Ximg, Yimg, 60, 10, way)
    image_plane(Ximg, Yimg)

    Ximg, Yimg = lens(Ximg, Yimg, 30, -10, way, 0)
    image_plane(Ximg, Yimg)
    m = Yimg / Yobj

    lim = plt.xlim()
    plt.plot([lim[0], lim[1]], [0, 0], 'k', linewidth=1.5)
    plt.gcf().canvas.draw()  # ensures limits are respected before showing
    plt.show()


if __name__ == "__main__":
    main()
