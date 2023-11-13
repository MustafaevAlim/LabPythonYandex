def merge(first, second):
    lst = list(first) + list(second)
    ans = []
    while len(lst) != 0:
        ans.append(min(lst))
        lst.remove(min(lst))
    return tuple(ans)

