marks = int(input("enter the marks: "))
if(marks>=90 and marks<=100):
    print("grade=A")
elif(marks>=80 and marks<90):
    print("grade=B")
elif(marks>=70 and marks<80):
    print("grade=C")
elif(marks>=60 and marks<70):
    print("grade=D")
else:
    if(marks>100):
        print("invalid marks")
    elif(marks<=-1):
        print("invalid marks")
    else:
        print("FAIL")

