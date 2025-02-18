#syntax:lamda arguments:expressiom
s1='akshayanisuman'
s2=lambda func:func.upper()
print(s2(s1))

#check number is positive or negative or zero
num=lambda x: 'positive' if x>0 else 'negative' if x<0 else 'zero'
print(num(5))
print(num(-5))
print(num(0))

square=lambda x: x**2
print(square(7))

list1=[lambda arg=x:arg*10 for x in range(1,5)]
for i in list1:
    print(i())
    print('ak')

#add and mul in single line
cal=lambda x,y:(x+y,x*y)
res=cal(5,6)
print(res)



