#!/usr/bin/python3
def uniq_add(my_list=[]):
    g = my_list[:].sort()
    filter(lambda x: g.remove(x) is None and g.count(x) == 0, my_list)
    print(g)
    return (sum(g))
