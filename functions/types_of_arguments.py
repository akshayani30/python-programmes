#1. Positional Arguments: These are the most basic type of arguments.
def greet(name, age): # formal parameters
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 25) #actual parametrs (4 types).

# 2.Keyword Arguments: Order doesn't matter when using keyword arguments. 
greet(age=30, name="Bob") 

#3. Default Arguments: 
#These arguments are assigned a default value in the function definition. 
#If no value is provided during the function call, the default value is used. 

def greet(name, age=30):
    print(f"Hello, {name}. You are {age} years old.")

greet("Charlie")  # age defaults to 30

#4. Arbitrary Arguments (args): Variable leanth argument
#Used when you don't know in advance how many arguments will be passed to the function. 
#The *args parameter collects all positional arguments into a tuple. 

def sum_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4))

#5. Arbitrary Keyword Arguments (kwargs): Keyword Variable Arguments
#Used when you don't know in advance how many keyword arguments will be passed to the function. 
#The **kwargs parameter collects all keyword arguments into a dictionary. 

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="David", age=35, city="New York") #one * for age, other * for 35, key:val