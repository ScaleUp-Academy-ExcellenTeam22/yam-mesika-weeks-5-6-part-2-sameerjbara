def interleave(*iterable):
    """:return interleave of the objects
            Args:
                *iterable (iterable): one iterable object or more .
            Returns:
                list: interleave of the objects.
            Raises:
                none.
            Examples:
                 interleave of 'abc' and [1,2,3] is ['a',1,'b',2,'c',3] .

                >>> print(interleave('abc', [1, 2, 3],('!','@','#')))
                ['a', '1', '!', 'b', '2', '@', 'c', '3', '#']

            """
    return [item[index] for index in range(0, len(iterable))
            for item in iterable if len(item) > index]


interleave('abc', [1, 2, 3], ('!', '@', '#'))
