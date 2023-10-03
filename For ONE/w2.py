a=5
b=20
if(a>b):
    print("a shall be the one")
else:
    print("b shall be the one")

if(a%2!=0 and a>b):
    print("a is odd so next is ",a+1)
elif(a%2==0 and a>b):
    print("a is even so next is ",a+2)
if(b%2!=0 and b>a):
    print("b is odd so next is ",b+1)
elif(b%2==0 and b>a):
    print("b is even so next is ",b+2)