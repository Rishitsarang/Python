# 8. Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

numbers = [10, 20, 30, 10, 20, 40, 10, 50, 30, 20]

print("Original list:", numbers)

# Empty dictionary to store counts
count_dict = {}

# Iterate list and count occurrences
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print("Occurrence of each element:", count_dict)
