n = int(input())
max_n = (n + 1) // 2
max_len = len(str(max_n))
for i in range(0, n // 2 + n % 2):
    number = 1
    length = len(str(number))
    for j in range(i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
        number += 1
        length = len(str(number))
    for j in range(n - 2 * i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
    number -= 1
    length = len(str(number))
    for j in range(i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
        number -= 1
        length = len(str(number))
    print()
for i in range(n // 2 - 1, -1, -1):
    number = 1
    length = len(str(number))
    for j in range(i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
        number += 1
        length = len(str(number))
    for j in range(n - 2 * i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
    number -= 1
    length = len(str(number))
    for j in range(i):
        print(f"{' ' * (max_len - length)}{number}", end=" ")
        number -= 1
        length = len(str(number))
    print()
        
    
