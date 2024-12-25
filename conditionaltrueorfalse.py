


a = int(input("a:"))
G = input("m/f : ")
if((a == 1 or a == 2) and G == 'm') :
    print("fee is 100")
elif((a == 3 or a == 4) and G == "f"):
    print("fee is 200")
elif(a == 5 and G == "m"):
    print("fee is 300")
else:
    print("no fee")
 
