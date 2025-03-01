# print(id(list2))
a=[1,2,3]
b=a
b.append(4)
print(a)

input="3[a]2[bc]"

ex="3[a2[c]]"

c='3'
d=int(c)+5
print(d)

e=0.1
f=0.2
g=0.3
print((e+f)==g)

fruits=["mango","apple","banana"]  #convert a list into string
print("".join(fruits))

print('hello'[1]) 

print(5-2+3*7)

z=[10,20,30,40,50,60,70]
i=0
while(i<len(z)):
#for i in z:
    z.remove(z[i])
    i=i+1
print(z)
print(type(z))


x=True+True+False
y=True+False+False
print(x,y)

n="89423"
m=max(n)
print(m)