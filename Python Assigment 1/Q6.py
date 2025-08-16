# 6. Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list


list1 = [10, 20, 30, 40,10]
poped=list1.pop(4)
print(list1)
list1.insert(2,poped)
print(list1)
list1.append(poped)
print(list1)