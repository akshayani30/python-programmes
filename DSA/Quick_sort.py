#divide and conquer algorithm
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[len(arr) // 2]  #middle ele as pivot
        left=[x for x in arr if x < pivot]
        middle=[x for x in arr if x == pivot]
        right=[x for x in arr if x> pivot]
        return quick_sort(left) + middle + quick_sort(right)
arr=[3,1,5,6,3,8,]
print(f"original array:{arr}")
sorted_arr=quick_sort(arr)
print(f"sorted arr:{sorted_arr}")