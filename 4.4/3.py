from itertools import combinations

def find_pair(*numbers, div=6):
    max_sum = -100000000000
    ans = 0
    for i in combinations(numbers[::-1], r = 2):
        print(list(i))
        if (sum(i) > max_sum) and (sum(i) % div == 0) :
            ans = (i[0], i[1])
            max_sum = sum(i)
    return f'{ans[1]} {ans[0]}'

print(find_pair(1,2,3,4,5, div=3))