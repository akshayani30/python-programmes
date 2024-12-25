terms=int(input("nuber of terms:"))
a=0
b=1
print(a)
print(b)
for i in range(2,terms):
    c=a+b
    print(c)
    a=b
    b=c
