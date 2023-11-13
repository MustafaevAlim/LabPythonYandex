def is_palindrome(value):
    if type(value) is int:
        if str(value) == str(value)[::-1]:
            return True
    else:
        if value == value[::-1]:
            return True
    return False

print(is_palindrome([1, 2, 1, 2, 1]))
    