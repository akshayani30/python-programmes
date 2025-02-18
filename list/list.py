list=[1,2,3]
print(list)
print(id(list))

list.append(4)
print(list)
print(id(list))
list2=list
list2.append(5)
print(id(list2))

