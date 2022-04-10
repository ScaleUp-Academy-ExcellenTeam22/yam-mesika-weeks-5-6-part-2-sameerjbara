def check_if_perfect_division(num):
    """"this function accepts a number, and check
     if the sum of all the numbers that can be divided by the given number
     is equal to the number  """
    sum = 0
    for divisor in range(1, round(num / 2) + 1):
        if num % divisor == 0:
            sum += divisor
            if sum == num:
                return "true"
            elif sum > num:
                return "false"
    return "false"


def print_all_perfect_division():
    """" this function print all the numbers that's considered a perfect division"""
    num = 1
    while "true":
        if check_if_perfect_division(num) == "true":
            print(num)
        num += 1


print_all_perfect_division()
