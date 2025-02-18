# *args (Non-keyword variable-length arguments)

def sum_num(*numbers):
    sum=0
    for num in numbers:
        sum +=num
    print(sum)
    
sum_num(1,2,3,4,5)


# **kwargs (Keyword variable-length arguments)
#returns as dictionary
def details(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

    print(f"name: {kwargs.get('name')}")  #accessing individual
details(name='ak',age='20')