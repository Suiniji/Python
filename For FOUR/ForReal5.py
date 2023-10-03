a = int(input())

s=a%1000
c=s%100
s-=c
s=s//100

print(s)