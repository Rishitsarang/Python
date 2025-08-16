# 12. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

numbers = [10, 20, 33, 46, 55, 75, 150, 180, 200, 250]

print("Numbers divisible by 5:")

for num in numbers:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)
