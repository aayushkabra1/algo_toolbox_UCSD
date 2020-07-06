# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    ps = [(x, "p") for x in points]
    ls = [(x, "l") for x in starts]
    rs = [(x, "r") for x in ends]

    counts = []
    new_list = []
    new_list.extend(ps)
    new_list.extend(ls)
    new_list.extend(rs)
    new_list = sorted(new_list)

    number_of_ls = 0
    number_of_rs = 0
    for element in new_list:
        if element[1] == "p":
            counts.append(number_of_ls - number_of_rs)
        if element[1] == "l":
            number_of_ls += 1
        if element[1] == "r":
            number_of_ls += 1

    return counts


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
