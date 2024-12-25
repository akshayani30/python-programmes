#sum of n terms
# n=5
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("sum:",sum)




n=123
sum=0
while n>0:
    sum+=n%10
    n//=10
print("sum:",sum)
