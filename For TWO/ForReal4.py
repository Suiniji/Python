a = int(input())
b = int(input())
s=0
for i in range(a,b+1):
    if(i%5==0):
        s=s+i
print(s)