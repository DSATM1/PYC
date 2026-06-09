#print("Hello World!")

"""n = int(input("Enter size: "))
nums = []
for i in range(n):
    value = input("Enter Names: ")
    nums.append(value)
print(nums)
for i, name in enumerate(nums):
     print(f"{i+1}. {name}")"""

"""odds = [i for i in range(1, 21) if i % 2 == 1]
print(odds)"""

"""def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
lst = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(lst)
print(result)"""

age,name,city = input("Enter your age, name, city:").strip().split()
age =int(age)
name = name
city = city

print("Your age:", age)
print("Your city:", city)
print("Your name:", name)