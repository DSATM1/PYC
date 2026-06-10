#print("List Practice Set")

"""reverse_list([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
   reverse_list(["a", "b", "c"]) → ["c", "b", "a"]"""


"""reverse_list = []
i = len(lst) - 1
while i >= 0:
   reverse_list += lst[i]
   i = i - 1
return reverse_list"""

def reverse_list(lst): #type:ignore
   res = []
   i = len(lst) - 1  #type:ignore
   while i>= 0:
      res.append(lst[i])  #type:ignore
      i = i - 1
   return res #type:ignore
print(reverse_list([1, 2, 3, 4, 5])) #type:ignore
print(reverse_list(["a","b","c","d","e"])) #type:ignore
