List = [2, 3, 5, 9, 3]
def summa(my_list):
    i = 1
    s = 0
    while i < len(my_list):
        s += my_list[i]
        i += 2
    print(s)
        
print(List)
summa(List)
