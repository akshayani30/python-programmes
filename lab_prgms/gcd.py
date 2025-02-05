def gcd_of_num(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    elif n1==n2:
        return n2
    else:
        if n1>n2:
            small=n2
        else: 
            small=n1
        for i in range(1,small+1):
            if n1%i==0 and n2%i==0:
                gcd=i
        return gcd

a=int(input("enter n1:"))
b=int(input("enter n2:"))
print(gcd_of_num(a,b))