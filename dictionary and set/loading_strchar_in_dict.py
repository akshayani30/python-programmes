str1=input("enter the word:")
freq={}
for i in str1:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1
print(freq)
for i in range(len(freq)):
    max_val=0
    max_char=''
    for key,value in freq.items():
        if value>max_val:
            max_val=value
            max_char=key
    print(max_char,end=":")
    print(max_val)
    # print(freq)

    freq[max_char]=0
print(freq)