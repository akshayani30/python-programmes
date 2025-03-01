arr=[10,20,30,40,50]
n=len(arr)
iterations=10
for i in range(iterations):
    circular_index=i%n
    print(arr[circular_index])