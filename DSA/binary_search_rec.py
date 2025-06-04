
def binary_search_rec(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binary_search_rec(arr,low,mid-1,x)
        else:
            return binary_search_rec(arr,mid+1,high,x)
    else:
        return -1
arr=[1,2,3,4,5,6,7,8]
x=5
result = binary_search_rec(arr, 0, len(arr)-1, x)
print(result)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")