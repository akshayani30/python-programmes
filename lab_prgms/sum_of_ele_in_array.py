def sum_of_array(n,arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
n=int(input("enter the size:"))
arr=list(map(int,input("enter numbers with spaces").split(',')))[:]
print(sum_of_array(n,arr))

# arr=input("enter the num :")[:n]
# print(arr)
