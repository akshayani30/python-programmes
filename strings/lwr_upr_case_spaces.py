name='akshayani'
print(name.upper())
bava="SUMAN"
print(bava.lower())

ak="I love u bava"  #convert them and give me upper/lower letter, space count
suman=""
uppcount=0
lowcount=0
spacecount=0
for i in ak:
    if i>'A' and i<'Z':
        uppcount +=1
        suman += chr(ord(i)+32)
   
    elif i.islower():
        lowcount +=1
        suman += (i.upper())

    elif i ==" ":
        spacecount +=1
        suman += i
#print(ak.swapcase())
print(ak)
print(uppcount)
print(lowcount)
print(spacecount)
print(suman)

