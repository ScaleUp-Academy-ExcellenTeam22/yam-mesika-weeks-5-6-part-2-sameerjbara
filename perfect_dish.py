def check_if_perfect_division(num):
    """Return true if the number is a perfect divison
       that means if the sum of all the numbers that can be divided by the given number
       is equal to the number.
                Args: num (int) : the number we want to check
                Returns: true/false (bool) : true if perfect divison else false
                Raises: none
                Examples:
                    16 is considred perfect divison
                    >>> print(check_if_perfect_division(16))
                    "true"
                """
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
    """Print all the numbers that's considered a perfect division (.
            Args: none
            Returns: none
            Raises: none
            Examples:
                6,24,28 is considred perfect divison

                >>> print_all_perfect_division()
                6 24 28 496 ...
            """
    num = 1
    while "true":
        if check_if_perfect_division(num) == "true":
            print(num)
        num += 1


print_all_perfect_division()
