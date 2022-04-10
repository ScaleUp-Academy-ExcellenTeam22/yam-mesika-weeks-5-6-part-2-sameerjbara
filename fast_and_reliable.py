import time

"""intit the list and the set"""
words_list = []
words_set = set()
file = open('words.txt')
for word in file:
    words_list.append(word)
    words_set.add(word)


def search(words):
    """ this function search the word "zwitterion"
     in the given data structure
     and return the time that took the function to preform the task  """
    start = time.time()

    for i in range(1, 1000):
        "zwitterion" in words

    end = time.time()
    return (end - start)



print(search(words_set))
print(search(words_list))
