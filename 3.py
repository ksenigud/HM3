my_list = [1.1, 1.2, 3.1, 10.01]
new_list = []
i = 0

while i < len(my_list):
     a = my_list[i] % 1
     new_list.append((round(a, 2)))
     i += 1

print(max(new_list) - min(new_list))