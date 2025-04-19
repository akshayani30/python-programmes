class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class D:
    varD="welcome to class D"
class C(A,B,D):                  
    varC="welcome to class C"

c1=C()
print(c1.varD)
