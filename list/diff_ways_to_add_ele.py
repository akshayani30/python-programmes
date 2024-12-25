#APPEND METHOD
list1= [1,2,3,4]
list1.append(5)
print(list1)

#INSERT METHOD
list2=[1,2,3,4]
list2.insert(4,5)
print(list2)

#EXTEND METHOD
list3=[1,2,3,4]
list3.extend([5])
print(list3)


#CONCATINATION
list4=[1,2,3,4]
#list5=[5]
#list4= list4 + list5
list4=list4 + [5]  
print(list4)

#adding no of elements by taking user input using loop
list =[1,2,3,4]
n=int(input("enter the no of elements:"))
for el in range (n):
    list.append(int(input("enter element")))
print(list)

