def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        mid = int(len(array) / 2)
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)
        

def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res