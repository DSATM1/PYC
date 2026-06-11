#print("List Practice Set")

"""reverse_list([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
   reverse_list(["a", "b", "c"]) → ["c", "b", "a"]"""

"""def reverse_list(lst): #type:ignore
   res = []
   i = len(lst) - 1  #type:ignore
   while i>= 0:
      res.append(lst[i])  #type:ignore
      i = i - 1
   return res #type:ignore
print(reverse_list([1, 2, 3, 4, 5])) #type:ignore
print(reverse_list(["a","b","c","d","e"])) #type:ignore"""


"""lst = [1, 2, 3, 4, 5]

reverse_list = []

i = len(lst) - 1

while i >= 0:
    reverse_list.append(lst[i])
    i = i - 1

print(reverse_list)"""

"""def palindrome(pal):
    return pal == pal[::-1]
res = palindrome("madaM")
print(res)"""



"""is_fail = True
i = 0
while is_fail:
   if i%2 != 0:
      i += 1
      continue
   print(f"Try {i}")
   i += 1
   if i>=10:
      break
print("Stop Loop Ended")"""


"""i = 1
while i <= 5:
   print(i * " SP ")
   i += 1"""


"""i = 0
while i <= 5:
   x = 1
   while x<i:
      print(f" S P {i} ",end = "")
      x = x+1
   print("")
   i += 1"""
      


