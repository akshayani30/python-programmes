def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print("ele is",arr[i],"found at index",i)
            return 
    print("element not found")   

arr=[1,2,3,4,5]
target=4



