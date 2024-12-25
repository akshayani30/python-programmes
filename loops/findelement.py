tuple = (1,2,3,4,5)
x=5  #this we have check is there or not in tuple
i=0
while i < len(tuple):
    if(tuple[i] == x):
        print("found at index",i)
        break   #if we use break whwn it satisfies if condn then it comes out from it
    else:
        print("finding..")
    i += 1
