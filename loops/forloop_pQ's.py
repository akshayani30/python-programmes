#syntax
list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)


#find x
num=(1,4,9,16,25,36,49,64,81,100,49)
x=100
i=0
for el in num:
    if(x == el):
        print("number found at:",i)

    i+=1