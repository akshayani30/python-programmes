my_list = [1, 2, 3, 4, 5]

# Calculate the middle index
middle = len(my_list) // 2

# Iterate and swap elements
for i in range(middle):
    temp = my_list[i]    #temp=1 temp=2 
    my_list[i] = my_list[len(my_list) - i - 1]  #list[0]=5   list[1]=4
    my_list[len(my_list) - i - 1] = temp    #list[4]=1   list[3]=2

print(my_list)


n=len(my_list)
i=0
while i<n/2:
    first,last=my_list[i],my_list[n-i-1]
 # last=my_list[n-i-1]
    my_list[n-i-1]=first
    my_list[i]=last
    i+=1
print(my_list)