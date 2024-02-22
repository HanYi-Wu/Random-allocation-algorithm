import random


def split_number(num):
    split_points = sorted(random.sample(range(1, num), 3))

    parts = [split_points[0], split_points[1] - split_points[0], split_points[2] - split_points[1],
             num - split_points[2]]

    return parts


number = 9987  # number to split
result = split_number(number)
print(result)
