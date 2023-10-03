def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    if n == 1:
        return False
    return True

n = int(input())
ans = 0
for i in range(n):
    b = int(input())
    if is_prime(b):
        ans += 1
print(ans)