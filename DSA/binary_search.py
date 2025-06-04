def binary_search(arr,x,low,high):
    while low <=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7]
x=4
result=binary_search(array,x,0,len(array)-1)
if result!=-1:
    print("element",x, "is present at index "+str(result))
else:
    print("not found")

