

x_1, y_1, x_2, y_2 = float(input()), float(input()),\
                     float(input()), float(input())


def distance(x_1, y_1, x_2, y_2):
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5


print('{0:.5f}'.format(distance(x_1, y_1, x_2, y_2)))
