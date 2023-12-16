from itertools import combinations

def find_pair(*numbers, div=2):
    max_sum = -100000000000
    for j in range(len(numbers) + 1):
        for i in combinations(numbers, r = j):
            if (sum(i) > max_sum) and (sum(i) % div == 0):
                max_sum = sum(i)
    return max_sum

print(find_pair(1,2,3,4,5))