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

"""age,name,city = input("Enter your age, name, city:").strip().split()
age =int(age)
name = name
city = city

print("Your age:", age)
print("Your city:", city)
print("Your name:", name)"""

"""day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")"""
        
"""x = 10
y = 5

match x + y:
    case 15:
        print("Result is 15.")
    case 20:
        print("Result is 20.")
    case _:
        print("No match found.")"""

"""grade = 'A'

match grade:
    case '0':
        print("Excellent!")
    case 'B':
        print("Good!")
    case _:
        print("Not specified.")"""