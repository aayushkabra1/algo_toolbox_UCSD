# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(first_num, second_num):
    big  = max(first_num, second_num)
    small = min(first_num, second_num)
   
    while(small):
        big, small = small, big%small

    return big

def lcm(a, b):
    return int((a*b)/(gcd(a, b)))

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

