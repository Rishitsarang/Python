# 7. Given a list slice it into a 3 equal chunks and reverse each list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", numbers)

# Length of each chunk
chunk_size = len(numbers) // 3  

# Slice into 3 chunks and reverse using slicing
chunk1 = numbers[0:chunk_size][::-1]
chunk2 = numbers[chunk_size:2*chunk_size][::-1]
chunk3 = numbers[2*chunk_size:][::-1]

print("After slicing and reversing:")
print("Chunk 1:", chunk1)
print("Chunk 2:", chunk2)
print("Chunk 3:", chunk3)
