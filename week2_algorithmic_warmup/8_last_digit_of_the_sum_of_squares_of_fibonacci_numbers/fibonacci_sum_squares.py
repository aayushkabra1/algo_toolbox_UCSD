# Uses python3
from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fib_sum(n):
    per = pisanoPeriod(10)
    rem1 = n % per
    rem2 = (n+1) % per

    f = [0, 1]
    for i in range(2, max(rem1, rem2) + 1):
        f.append(f[i-1] + f[i-2])

    Rem1 = f[rem1] % 10
    Rem2 = f[rem2] % 10

    return (Rem1*Rem2) % 10    


if __name__ == '__main__':
    n = int(stdin.readline())
    print(fib_sum(n))
