def find_special_state():
    """ this function run on a file that contains names of states
     and check which state name can be written only by on line in the keyboard"""
    keyBoard = {'qwertyuiop', 'asdfghjkl', 'zxcvbnm'}
    file = open('states.txt')
    for state in file:
        for keyline in keyBoard:
            if state <= keyline:
                return state

    return "none"


print(find_special_state())