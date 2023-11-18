ints = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
print([i for i in ints if int(str(i)[-1]) > 3] + [i for i in ints if int(str(i)[-1]) <= 3])