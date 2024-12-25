list=[1,2,3]
list2=[0]*(len(list)+1)
index=int(input("enter the index position:"))   #let index=2
value=int(input("enter the index value:"))    #value=7
j=0
for i in range(len(list2)):    #i from 0 to last vaue
    if(i==index):   #i=0 not satisfies, i=1=!index,i=2   ,i=3=!index
        list2[i]=value                 #list2[2]=value,
    else:
        list2[i]=list[j] #list2[0]=1 ,list2[1]=2          list[3]=3
        j+=1

print(list2)

