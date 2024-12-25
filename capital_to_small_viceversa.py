string=input("enter the string:")
new_string= ""
for i in range(len(string)):
    if string[i]>='a' and 'z'>=string[i]:
        new_string+=chr(ord(string[i])-32)
    elif string[i]>='A' and 'Z'>=string[i]:
        new_string+=chr(ord(string[i])+32)
    else:
        new_string+=string[i]
print(new_string)
