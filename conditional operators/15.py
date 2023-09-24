n = int(input())
m = int(input())

n_1 = n % 10
n_2 = n // 10
m_1 = m // 10
m_2 = m % 10

a1 = max(n_1, n_2, m_1, m_2)
a3 = min(n_1, n_2, m_1, m_2)
a2 = ((n_1 + n_2 + m_1 + m_2) - (a1 + a3)) % 10

print(str(a1) + str(a2) + str(a3))

