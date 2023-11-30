def to_string(*string, sep=' ', end='\n'):
    result = ''
    for i in string:
        result += str(i) + sep
    result = result.rstrip(sep)
    result += end
    return result

