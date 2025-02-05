def lcm(n1,n2):
    multiple=max(n1,n2)
    while True:
        if multiple%n1==0 and multiple%n2==0:
            return multiple
        multiple+=1
n1=int(input())
n2=int(input())
result=lcm(n1,n2)
print(result)
