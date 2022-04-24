import itertools
import numpy as np


def interleave(*iterable):
    """yields each time different interleave of the objects
       by mergeing all the permutations of each object.
            Args:
                *iterable (iterable): one iterable object or more .
            Yields:
                list: one interleave of the objects.
            Raises:
                none.
            Examples:
                one posible interleave of 'abc' and [1,2,3] is ['a',1,'b',2,'c',3] .

                >>> generator = interleave('abc', [1, 2, 3],('!','@','#'))
                >>> print(next(generator))
                ['a', '1', '!', 'b', '2', '@', 'c', '3', '#']

            """

    objects_permutations = [list(itertools.permutations(item, len(item))) for item in iterable]
    permutations_number = len(objects_permutations[0])
    objects_merged_permutations = \
        np.array_split([val for tup in zip(*objects_permutations) for val in tup], permutations_number)
    # in order to get in each index of the list a one permutation of each object
    for i in range(0, len(objects_merged_permutations)):
        yield [val for tup in zip(*objects_merged_permutations[i]) for val in tup]


generator = interleave('abc', [1, 2, 3], ('!', '@', '#'))
print(next(generator))
