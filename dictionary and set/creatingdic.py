null_dic ={}
print(null_dic)    #adding the values in empty dictionary

null_dic["name"] ="akshayani"
print(null_dic)


#NESTED DICTIONARY
student = {"name":"akshayani","marks":{"chem":100,"phy":90,"math":95}  }
print(student)
print(student["marks"])  #printing nested dict
print(student["marks"]["math"])   #here printing  particular marks in nested dict

print(student.keys())  #it prints all keys in dict not nested keys
print(len(student))    #length equa to total no of keywords