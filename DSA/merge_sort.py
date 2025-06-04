def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]

    sortedleft=mergesort(lefthalf)
    sortedright=mergesort(righthalf)

    return merge(sortedleft,sortedright)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
unsortedarray=[1,4,2,3,6,7,9,0]
sortedarray=mergesort(unsortedarray)
print("sorted array:",sortedarray)