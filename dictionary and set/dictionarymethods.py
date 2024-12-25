
student = {"name":"akshayani","marks":{"chem":100,"phy":90,"math":95}  }
print(student)
print(student["marks"])  #printing nested dict
print(student["marks"]["math"])   #here printing  particular marks in nested dict

print(student.keys())  #it prints all keys in dict not nested keys
print(len(student))    #length equa to total no of keywords
print(student.values())   #except keywords it print values
print(student.items())   #it prints keyword and value as pair(key,val)
print(student.get("name"))  #it print value according to key we have mention
print(student["name"])     #line 12 and 13 output both are same only when keys are present in dict
print(student.get("name"))
student.update({"age": 19})
print(student)