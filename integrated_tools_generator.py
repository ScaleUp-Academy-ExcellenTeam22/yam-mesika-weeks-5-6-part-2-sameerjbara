import itertools

def interleave(*iterable):
    """ get one iterable object or more and merge the objects contents """
    permuts=[]
    merged=[]
    for item in iterable:
     permut = itertools.permutations(item, len(item))
     permuts.append(list(permut))
    index1=0
    index2=0
    while index2<len(permuts[index1]):
        while index1 <len(permuts) :
            merged.append(permuts[index1][index2])
            index1+=1
        q=[val for tup in zip(*merged) for val in tup]
        yield q
        merged.clear()
        index1=0
        index2+=1

gen=interleave('abc', [1, 2, 3],('!','@','#'),('Q','W','E'))
print(next(gen))


