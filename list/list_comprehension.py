a=[1,2,3,4,5]
result=[val ** 2 for val in a]
print(result)

a=[1,2,3,4,5]
result=[] #creating empty list
for val in a:
    result.append(val * 2)
print(result)

a=[1,2,3,4,5]
result=[val for val in a if val % 2 == 0]
print(result)

#creates a list of numbers from 0 to 9
a=[i for i in range(10)]
print(a)

#creates a list of tuples representing all combinatons all combinations (x,y)
coordinates=[(x,y) for x in range(4) for y in range(4)]
print(coordinates)

mat=[[1,2,3],[4,5,6],[7,8,9]]
result=[val for sublist in mat for val in sublist]
print(result)