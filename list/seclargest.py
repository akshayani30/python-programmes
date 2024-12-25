list=[2,5,1,3,7,8]
if list[0]>list[1]:
    max1=list[0]
    max2=list[1]
else:
    max1=list[1]
    max2=list[0]
for i in range(2,len(list)):
    if list[i]>max1:
        max2=max1
        max1=list[i]
    elif list[i]>max2 and list[i]<max1:
        max2=list[i]
print(max2)
print(max1)