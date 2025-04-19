def linear_search_recursive(arr, target, index=0):
    
    if index >= len(arr):
        return -1  # Base case: target not found

    if arr[index] == target:
        return index  # Base case: target found

    return linear_search_recursive(arr, target, index + 1)  # Recursive step


my_list = [5, 1, 9, 3, 7, 6]
target_element = 9

# Using recursive linear search
result_recursive = linear_search_recursive(my_list, target_element)
if result_recursive != -1:
    print(f"Element {target_element} found at index {result_recursive} (recursive)")
else:
    print(f"Element {target_element} not found in the list (recursive)")


# def linear_search(arr,target,i=0):
#         if i==len(arr):
#               print("ele not found")
#               return
#         if arr[i]==target:
#             print("ele is",arr[i],"found at index",i)
#             return
        
#         linear_search(arr,target,i+1)
    


# arr=[1,2,3,4,5]
# target=2
# linear_search(arr,target)
