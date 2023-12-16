def add_number(number):
    x.append(number)

def prod(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

def get_prod():
    s = ''
    for i in x:
        s += str(i) + ' * '
    s = s[:-3] + " = " + str(prod(x))
    return s

x = []
add_number(1)
add_number(2)
add_number(3)
add_number(3)
print(get_prod())