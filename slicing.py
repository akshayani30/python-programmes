str='akshayanisuman'
substring = str[9:14]


print('sub string:',substring)

print(str[0:len(str)])    #using length function
print(str[:6])        #if we not write starting index automatically it takes
print(str[0:])            #if we not mention last index automatically it takes
print(str[:])      #if we not mention first and last index automatically it takes

#NEGATIVE SLICING
str2="suman"
print(str2[-3:-1])
print(str2[-6:-1])