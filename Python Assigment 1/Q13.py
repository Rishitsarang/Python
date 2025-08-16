# 13. Reverse the following list using for loop

# List1 = [10,20,30,40]

List1 = [10, 20, 30, 40]
reversed_list = []

print("Original list:", List1)

# Iterate backwards using range
for i in range(len(List1) - 1, -1, -1):
    reversed_list.append(List1[i])

print("Reversed list:", reversed_list)
