s1 = input()
s2 = input()
s3 = input()

s1_zayka = 'зайка' in s1
s2_zayka = 'зайка' in s2
s3_zayka = 'зайка' in s3
ans_1 = 10000000000
ans_2 = 10000000000
ans_3 = 10000000000

if s1_zayka:
    ans_1 = len(s1)
if s2_zayka:
    ans_2 = len(s2)
if s3_zayka:
    ans_3 = len(s3)


if s1 < s2 and s1 < s3:
    print(s1, ans_1)
elif s2 < s1  and s2 < s3:
    print(s2, ans_2)
elif s3 < s1 and s3 < s2:
    print(s3, ans_3)