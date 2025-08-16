# 2. Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

start = 1
end = 10
previous = 0 

for current in range(start, end + 1):
    print(f"Current: {current}, Previous: {previous}, Sum: {current + previous}")
    previous = current
