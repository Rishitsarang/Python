# 1. Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = num1 * num2

if product > 1000:
    result = num1 + num2
else:
    result = product

print("Result:", result)
