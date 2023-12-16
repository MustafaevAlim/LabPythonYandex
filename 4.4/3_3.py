from itertools import combinations

def find_pair(*numbers, div=10):
    ans = 0
    for i in combinations(numbers, r = 2):
        print(list(i))
        if (sum(i) % div == 0) :
            ans += 1
    return ans

print(find_pair(1,2,3,4,5, div=10))