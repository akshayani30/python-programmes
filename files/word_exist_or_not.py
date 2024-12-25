word="hello"
# with open("ak.txt","r") as f:
f=open("ak.txt","r")
data=f.read()
if word in data:
        print("found")
else:
        print("not found")




