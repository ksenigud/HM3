my_list1 = [2, 3, 4, 5, 6]
my_list2 = [2, 3, 5, 6]

def proisv (list):
     i = 0
     while i < len(list) / 2:
         a = list[i] * list[len(list) - 1 - i]
         print(f"{list[i]} * {list[len(list) - 1 - i]} = {a}")  
         i += 1

proisv(my_list1)
print()
proisv(my_list2)