list1=[1,2,3,4,5,6]
list2=[0]*(len(list1)+1)
print(list2)
for el in range(len(list1)):
    list2[el]=list1[el]
list2[(len(list2)-1)]=int(input("enter the ele which you want to add at last:"))
print(list2)