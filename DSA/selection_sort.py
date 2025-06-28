def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        temp=a[i]
        a[i]=a[min_index]
        a[min_index]=temp
a=[1,3,4,2,5]
# n=int(input("enter size of the array:"))
# print("enter elements of the array:")
# for _ in range(n):
#     element=int(input())
#     a.append(element)
selection_sort(a)
print("after sorting")
for num in a:
    print(num,end='')
    