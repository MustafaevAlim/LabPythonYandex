numbers = []
def enter_results(*n):
    global numbers
    numbers += n

def get_sum():
    s1 = [numbers[i] for i in range(0, len(numbers), 2)]
    s2 = [numbers[i] for i in range(1, len(numbers), 2)]
    return (round(sum(s1), 2), round(sum(s2), 2))

def get_average():
    s1 = [numbers[i] for i in range(0, len(numbers), 2)]
    s2 = [numbers[i] for i in range(1, len(numbers), 2)]
    return (round(sum(s1) / (len(s1)), 2), round(sum(s2) / len(s2), 2))

enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())