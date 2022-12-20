n = int(input('Enter number: '))
my_list = []

def binar (x, y):
    while x > 0:
         a = str(x % 2)
         y.append(a)
         x = x // 2
    y.reverse()
    print(" ".join(y))

binar(n, my_list)