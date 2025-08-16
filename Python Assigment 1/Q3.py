# 3. Given a string, display only those characters which are present at an even index number.

string = input("Enter a string: ")

print("Characters at even index are:")

for i in range(0, len(string), 2):
    print("Index[", i, "]", string[i])
