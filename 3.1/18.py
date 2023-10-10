s = input()

curr_sym = s[0]
curr_count = 0
for i in s:
    if curr_sym != i:
        print(curr_sym, curr_count)
        curr_count = 0
    curr_sym = i
    curr_count += 1
print(curr_sym, curr_count)