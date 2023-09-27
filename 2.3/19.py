my_list = list(range(1, 1001))
low = 0
high = len(my_list) - 1
while low <= high:
    mid = (low + high) // 2
    guess = my_list[mid]
    print(guess)
    many = str(input())
    if many == 'Угадал!':
        break
    elif many == 'Меньше':
        high = mid - 1
    elif many == 'Больше':
        low = mid + 1