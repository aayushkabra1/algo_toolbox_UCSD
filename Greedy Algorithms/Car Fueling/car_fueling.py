# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.append(d)
    for i in range(input_n, 0, -1):
        stops[i] = stops[i-1]    
    stops[0] = 0
    stops.append(d)
    # makes the stops list as [0, x1, x2, x3,....., xn, xn+1]
    # 0 as satrting point as xn+1 as target

    num_fills = 0
    current_pos = 0
    while current_pos <= input_n:
        last_pos = current_pos
        while current_pos <= input_n and stops[current_pos + 1] - stops[last_pos] <= m:
            current_pos += 1
        if current_pos == last_pos:
            return -1
        if current_pos <= input_n:
            num_fills += 1
    return num_fills                


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
