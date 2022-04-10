def interleave(*iterable):
    """ merge iterable objects"""
    merged_list=[]
    for index in range(0,len(iterable)):
        for item in iterable:
            if(len(item)>index):
             merged_list.append(item[index])
    print(merged_list)


interleave('abc', [1, 2, 3], ('!', '@','#'))