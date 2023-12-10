def make_linear(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, list):
            new_lst.extend(make_linear(i))
        else:
            new_lst.append(i)
    return new_lst