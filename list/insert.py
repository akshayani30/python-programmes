list=[1,2,3,4,5]
list2=[0]*(len(list)+1)
for i in range(len(list)):
    list2[i]=list[i]
print(list2)
index=int(input("enter the index position:"))    #2
i=len(list2)-1   #i=5
while i>=index:
    list2[i]=list2[i-1]
    i-=1
ele=int(input("enter the value:"))
list2[index]=ele
list=list2
print(list)
    