a=10
print(id(a))

def akshayani():
    a=9
    x=globals()['a']
    print(id(x))
    print(x)
    print(a)
    globals()['a']=15  #we can also change here from 10 to 15

akshayani()


b=10
def something():
    global x  #here converting local to global x 
    x=15
    print("in func:",b)
ak=something()
print("out func:",b)
print(x)
print(type(ak))