name=input("enter the word:")
maxfreq=0
for i in range(len(name)):
    currcount=1
    for j in range(i+1,len(name)):
        if(name[i]==name[j]):
            currcount+=1
    
    if(currcount>maxfreq):
        maxfreq=currcount
        ch=name[i]

    print("max repeated letter is",ch,"and is frequency is",maxfreq)
    maxfreq=0

