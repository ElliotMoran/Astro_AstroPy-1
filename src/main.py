from astropy.io import fits

import matplotlib.pyplot as plt


def main() -> None:
    x_star_coord = 1091
    y_star_coord = 1036
    x_delta = 10
    y_delta = 10

    x_start = x_star_coord - x_delta
    x_end = x_star_coord + x_delta
    y_start = y_star_coord - y_delta
    y_end = y_star_coord + y_delta
    
    image_data = fits.getdata('data/data.fit')

    x_value_list = []
    y_value_list = []

    for y in range(y_start, y_end):
        x_value_list.append(image_data[y][x_star_coord])

    for x in range(x_start, x_end):
        y_value_list.append(image_data[y_star_coord][x])
    
    fig, ax = plt.subplots(2)
    plt.subplots_adjust(hspace=1)

    ax[0].plot(range(x_start, x_end), x_value_list)
    ax[0].set_title('Dependence of value on x coordinate')
    ax[0].set_xlabel('Coordinate')
    ax[0].set_ylabel('Value')

    ax[1].plot(range(y_start, y_end), y_value_list)
    ax[1].set_title('Dependence of value on y coordinate')
    ax[1].set_xlabel('Coordinate')
    ax[1].set_ylabel('Value')

    fig.savefig('data/graph.png', dpi=250)


if __name__ == '__main__':
    main()

