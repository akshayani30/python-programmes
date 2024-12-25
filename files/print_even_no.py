count=0
with open("file.txt","r") as f:
    data=f.read()
    nums=data.split(",")   #["1","2","3",....]
    print(nums)     
    for value in nums:
        if(int(value)%2==0):
            print(value)
            count+=1
            
print("count:",count)