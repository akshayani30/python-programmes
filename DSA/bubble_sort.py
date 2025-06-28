def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):  #it shift large number to right side for first i iteration that's why its j iteration decreases
            if a[j]>a[j+1]:
                
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[1,3,5,2,7]
bubble_sort(a)
print("after sorting")
for num in a:
    print(num,end='')
