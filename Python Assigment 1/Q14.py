# 14. Write a Python program to display all the prime numbers within a range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:  # prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # check divisibility
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
