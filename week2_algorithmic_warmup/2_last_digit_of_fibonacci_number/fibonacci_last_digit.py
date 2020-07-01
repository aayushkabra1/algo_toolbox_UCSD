# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fib_last_digit(a):
    fib = [0, 1]
    for i in range(2, a+1):
        num = (fib[i-1] + fib[i-2]) % 10
        fib.append(num)

    return fib[a] % 10        

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fib_last_digit(n))
