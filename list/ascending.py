list=[1,2,4,3,5,7]
for i in range(len(list)):
    j=i+1
    for j in range(j,len(list)):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        # j+=1
    # i+=1

for i in range(len(list)):
    print(list[i])