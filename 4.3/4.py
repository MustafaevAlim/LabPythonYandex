def answer(f):
    def decor(*args, **kwargs):
        return f'Результат функции: {f(*args, **kwargs)}'
    return decor
