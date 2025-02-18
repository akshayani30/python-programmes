
def fact_num(n):
    print(id(n))
    n=6
    
    print("after:",id(n))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
a=5
b=a
c=5
print(id(a))
print(id(b))
print(id(c))
fact_num(a)
print(fact_num)