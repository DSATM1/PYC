# List Comprehension Examples

# Example 1: Basic list comprehension (Squares)
squares = [x**2 for x in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

# Example 2: List comprehension with a condition (Even numbers)
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers up to 20: {evens}")

# Example 3: String manipulation
words = ['hello', 'world', 'python', 'list', 'comprehension']
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Example 4: Nested list comprehension (Flattening a 2D matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")