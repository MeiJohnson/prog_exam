import itertools

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

res = list(itertools.islice(fib(), 15)) #  islice() модуля itertools создает итератор, который возвращает выбранные элементы из итератора iterable.
print(res)