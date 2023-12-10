def same_type(f):
    def decor(*args):
        for i in range(len(args) - 1):
            if type(args[i]) is not type(args[i+1]):
                print("Обнаружены различные типы данных")
                return None
        return f(*args)
    return decor

@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
            