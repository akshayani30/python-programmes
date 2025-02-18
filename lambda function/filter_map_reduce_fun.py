# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))


#lambda with map()
a=[1,2,3,4]
b=map(lambda x:x*2,a)
print(list(b))

#using reduce()
#summing numbers with reduce and  lambda
from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda x,y:x+y,a)
print(result)