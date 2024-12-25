def fact(n):
    if(n==1 or n==0):    #base case
        return 1
    else:
        return fact(n-1)*n
fact=fact(5)
print(fact)
        