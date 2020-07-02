# python3

from itertools import permutations

def largest_number(numbers):

    digits = []
    for num in numbers:
        number = int(num)
        while number >= 10:
            digit = number % 10
            digits.append(digit)
            number = number // 10
        if number < 10:
            digits.append(number)        

    ans = ""
    
    new_list = sorted(digits)

    for i in range(len(digits)):
        ans += str(max(digits))
        digits.remove(max(digits))

    return ans    


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
