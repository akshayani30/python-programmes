test_str = "sumanbava"
 
# printing original string
print ("The original string is : " +test_str)
all_freq = {}
for i in test_str:
    if i in all_freq:  #if  i in dictionary:
        all_freq[i] += 1
    else:
        all_freq[i]=1
print(all_freq)
for i in range(len(all_freq)):
    maxcou=0
    maxchar=""
    for key,value in all_freq.items():
        if maxcou<value:
            maxcou=value
            maxchar=key
    print(maxchar,end=":")
    print(maxcou)
    all_freq[maxchar]=0


  
        
