def make_matrix(tup, value=0):
    if type(tup) is int:
        result = [[value for j in range(tup)] for i in range(tup)]
    else:
        result = [[value for j in range(tup[0])] for i in range(tup[1])]
    return result


print(make_matrix((4, 4), 10))