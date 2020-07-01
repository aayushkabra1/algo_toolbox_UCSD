# Uses python3
import sys

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1
# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10

def fib_sum(m, n):
    fib = [0, 1]
    per = pisanoPeriod(10)
    rem1 = (m+1) % per
    rem2 = (n+2) % per

    for i in range(2, max(rem1, rem2) + 1):
        fib.append(fib[i-1] + fib[i-2])

    Rem1 = fib[rem1] % 10
    Rem2 = fib[rem2] % 10

    if Rem1 > Rem2:
        return 10 - (Rem1 - Rem2)

    else:
        return Rem2 - Rem1        
        

if __name__ == '__main__':
    input = sys.stdin.readline()
    from_, to = map(int, input.split())
    print(fib_sum(from_, to))