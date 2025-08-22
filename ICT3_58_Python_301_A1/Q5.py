# 5. Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

list1 = [10, 20, 30, 40, 10]
list2 = [100, 200, 300, 400, 100]
list3 = []

for i in range(max(len(list1), len(list2))):
    if i % 2 != 0:  
        if i < len(list1):
            list3.append(list1[i])
    elif i % 2 == 0: 
        if i < len(list2):
            list3.append(list2[i])

print(list3)
