list1 = ["code","bunny","YeS"]
x = list1.index(min(list1,key=len))
y = list1.index(max(list1,key=len))
list1 [x], list1 [y] = list1[y], list1[x]
print("Changed: ", list1)