# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    den1, den5, den10 = 0, 0, 0
    if money % 10 >=5:
        den5 = 1
        den1 = money%10 - 5

    else:
        den1 = money%10
        den5 = 0

    den10 = int(money/10)
    return den1 + den5 + den10


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
