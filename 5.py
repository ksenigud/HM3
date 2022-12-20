k = int(input('Enter number: '))

my_list_1 = [0, 1]
for i in range(k - 1):
    my_list_1.append(my_list_1[i] - my_list_1[i + 1])
my_list_1 = my_list_1[::-1]

my_list_2 = [0, 1]
for i in range(k - 1):
    my_list_2.append(my_list_2[i] + my_list_2[i + 1])

for i in range(1, k + 1):
    my_list_1.append(my_list_2[i])
print(my_list_1)