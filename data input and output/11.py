s = input()
first_part = s[0:2]
second_part = s[2:4]
s = first_part[::-1] + second_part[::-1]
print(s)