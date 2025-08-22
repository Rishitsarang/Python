# 9. Add a list of elements to a given set: {‘yellow’,’orange’} List:[blue,black]

# Given set and list
my_set = {"yellow", "orange"}
my_list = ["blue", "black"]

print("Original set:", my_set)
print("List to add:", my_list)

# Add list elements into set
my_set.update(my_list)

print("Updated set:", my_set)
