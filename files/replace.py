f=open("ak.txt","r")
data=f.read()

data1=data.replace("bava","sumanbava")
print(data1)

f=open("ak.txt","w")
f.write(data1)








