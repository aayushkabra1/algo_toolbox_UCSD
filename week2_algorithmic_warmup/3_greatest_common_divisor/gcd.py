# Uses python3
import sys


def gcd(first_number, second_number):
    if second_number == 0:
        return first_number
    else:
        rem = first_number % second_number
        return(gcd(second_number, rem))        

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a, b))
