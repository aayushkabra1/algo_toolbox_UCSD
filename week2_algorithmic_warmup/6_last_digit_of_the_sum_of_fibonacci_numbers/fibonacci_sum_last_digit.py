# Uses python3
import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

per = pisanoPeriod(10)
def fib_sum(n):

    rem = (n + 2) % per
    f = [0, 1]
    for i in range(2, rem + 1):
        f.append(f[i-1] + f[i-2])

    if f[rem] % 10 == 0:
        return 9
    else:
        return (f[rem] %10) -1        


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fib_sum(n))
