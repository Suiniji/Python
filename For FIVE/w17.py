list1 = ['monster','monster1','monster2']
list2 = list1.copy()
list3 = list1 + list2
list1.extend(list2)
print(list3)
print(list1)