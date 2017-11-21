lis = [1, 2, 3, 4]
print('lis', lis, ', whose id is', id(lis))

def func(list) :
    return id(list)

# call by value
print("* call by value     ->func(lis[:]), and id of input parameter is", func(lis[:]))
# call by reference
print("* call by reference ->func(lis), and id of input parameter is ", func(lis))


dic = {'1': 'a', '2': 'b'}
print('dic',dic, ', whose id is', id(dic))
# dictionary to list
l = []
[l.extend([i, j]) for i, j in dic.items()]
print(l)

# list to dictionary
d = {lis[i]:lis[i+1] for i in range(0, len(lis), 2)}
print(d)

