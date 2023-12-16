def add_number(number):
    x.append(number)

def get_sum():
    s = ''
    for i in x:
        s += str(i) + ' + '
    s = s[:-3] + " = " + str(sum(x))
    return s

x = []
add_number(1)
add_number(2)
add_number(3)
print(get_sum())