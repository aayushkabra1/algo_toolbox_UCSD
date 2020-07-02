# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    cost = 0
    for i in range(n):
        if capacity == 0:
            return cost

        max_value = prices[0]/weights[0]
        max_index = 0
        for j in range(n):
            if weights[j] > 0:
                if prices[j]/weights[j] > max_value:
                    max_value = prices[j]/weights[j]
                    max_index = j

        a = min(weights[max_index], capacity)
        capacity = capacity - a
        weights[max_index] = weights[max_index] - a
        cost = cost + a*max_value

    return cost


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
