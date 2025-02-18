def count_digits(n):
    if n<0:
        n=-n
    if n==0:
        return 1
    count=0
    while n>0:
        count+=1
        n//=10
    return count
n=int(input("enter the num:"))
print(count_digits(n))