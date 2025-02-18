# A Python program to return multiple 
# values from a method using dictionary 

# This function returns a dictionary 
def fun(): 
	d = {}  #we cam also create dict by dict() and dict();
	d['str'] = "GeeksforGeeks"
	d['x'] = 20
	d.update({'y':30})
	return d 

# Driver code to test above method 
d = fun() 
print(d) 
