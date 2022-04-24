def find_special_state():
    """:return list of the satates that can be writing by one keyline in the keyboard
                Args:
                    none.
                Returns:
                    list: list of the states that fulfill the condition.
                Raises:
                    none.
                Examples:
                     a state that can be writing by on keyline is alaska.
                    >>> print(find_special_state())
                    ['alaska']
                """
    key_board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    file = open('states.txt', "r").readlines()
    states = [line.rstrip('\n') for line in file]
    return ([state for state in states for key_board_line in key_board
             if check_if_substring(state, key_board_line) == "true"])


def check_if_substring(substring, string):
    """:return ture if the first srting is a sub string of the second string
                Args:
                    substring (str) : the string we want to check if its a substring.
                    string (str) : the full string
                Returns:
                    true/false (bool).
                Raises:
                    none.
                Examples:
                     "alaska" is a substring of "asdfghjkl".
                    >>> print(check_if_substring("alaska", "asdfghjkl"))
                    true
                """
    for letter in substring:
        if letter not in string:
            return "false"
    return "true"


print(find_special_state())
