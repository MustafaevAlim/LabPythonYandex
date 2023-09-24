n = int(input())

n1 = n // 100
n2 = (n % 100) // 10
n3 = n % 10

maxim = max(n1, n2, n3)
minim = min(n1, n2, n3)
sr = (n1 + n2 + n3) - (maxim + minim)

ans_maxim = str(maxim) + str(sr)
ans_minim = str(sr) + str(minim)

print(ans_minim, ans_maxim)