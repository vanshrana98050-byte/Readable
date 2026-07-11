a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))

if(a>b and a>c and a>d):
    print("a is greatest")
if(b>a and b>c and b>d):
    print("b is greatest")
if(c>a and c>b and c>d):
    print("c is greatest")
else:
    print("d is greatest")    