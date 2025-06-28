def insertion_sort(arr):
    for i in range(1,size):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]  #if its satisfies it checks sorted left side
            j-=1
        arr[j+1]=key

arr=[1,3,4,2,5]
size=len(arr)
# size=int(input("Enter the size of array: "))
# print("Enter the elements of array: ")

# for _ in range(size):
#     arr.append(int(input()))
insertion_sort(arr)

print("Sorted array is: ")
for i in range(size):
    print(arr[i],end=" ")
