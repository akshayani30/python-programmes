#to check if the given number is armstron are not
n=int(input("enter the number:"))
arm=0
initial=n       #0, 1, 153, 370, 371 and 407 are the Armstrong numbers
while n>0:
    rem=n%10
    # arm=(rem*rem*rem)+arm
    arm+=(rem*rem*rem*rem)
    n=n//10

if initial == arm:
    print("armstrong number")
else:
    print("not a armstrong number")