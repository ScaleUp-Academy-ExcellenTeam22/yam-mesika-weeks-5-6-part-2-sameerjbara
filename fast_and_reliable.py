import time


def compare_runtime():
    """Prints the average runtime for searching in different data structers
                    Args: none
                    Returns: none
                    Raises: none
                    Examples:
                        average runtime in set is - 0.0
                        average runtime in list is - 0.008217726230621338
                        >>> compare_runtime()
                        0.008217726230621338
                        0.0
                    """
    file = open('words.txt')
    words_list = [word for word in file]
    words_set = set(words_list.copy())
    print(average_runtime(words_list))
    print(average_runtime(words_set))
    file.close()


def average_runtime(words):
    """Returns the average runtime for searching 1000 time a word in a givin data structers
                        Args:
                            words (data struct) : the giving data structer
                        Returns:
                            int : the average run time for searching in the ds
                        Raises: 
                            none
                        Examples:
                            average runtime in set is - 0.0
                            >>> average_runtime(("aa","bb","cc","dd"))
                            0.0
                        """
    timer_start = time.time()
    for i in range(1, 1000):
        "zwitterion" in words
    timer_end = time.time()
    return (timer_end - timer_start) / 1000


compare_runtime()
