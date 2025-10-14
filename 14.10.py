import random

def create_random_list(_size, _min, _max):
    _list=[]
    for i in range(_size):
        _list.append(random.randint(_min,_max))
    return _list

def even_list(_list):
    list=[]
    for i in _list:
        if i%2==0:
            list.append(i)
    return list

list1 = create_random_list(8,10,99)
print(list1)
list2 = even_list(list1)
print(list2)
