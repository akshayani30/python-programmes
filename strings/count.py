
def compress_string():
    emp=[]
    str1=""
    for i in range(len(str2)):
        if str2[i] not in emp:
           # emp.append(str2[i])
           emp +=str2[i]
    print(emp)
    for k in emp:
        count=0
        for i in range(len(str2)):
            if(k ==str2[i]):
                count +=1

        str1 += str(count)+k
    return str1

str2="aaabbcab"
compressed_string=compress_string()
print(compressed_string)

