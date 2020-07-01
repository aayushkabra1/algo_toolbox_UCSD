# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m

def fib(n, m):
    per = pisanoPeriod(m)

    f = [0, 1]
    rem = n % per
    for i in range(2, rem + 1):
        f.append(f[i-1] + f[i-2])

    return f[rem] % m


def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1           

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(fib(n, m))
