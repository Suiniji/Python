list1 = ['monster','monster1','monster2']
list2 = list1.copy()

for x in list2:
  list1.extend(list2)

print(list1)