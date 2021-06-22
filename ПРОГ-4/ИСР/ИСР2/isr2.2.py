import functools

def deco(func):
    @functools.wraps(func)
    def wrap(*args):
        f = open('a2.out', 'w')
        print("Смотри, что я получил:", args[0], args[1], args[2])
        result = func(*args)
        name = ''
        if (args[2] == '+'):
            name = 'Сложение'
        if (args[2] == '-'):
            name = 'Вычитание'
        if (args[2] == '*'):
            name = 'Умножение'
        if (args[2] == '/'):
            name = 'Деление'
        f.write(f"{args[0]}, {args[1]}, {name}, {result}")
        f.close()
        return result
    return wrap

@deco
def calc(a,b,act):
    res = 0
    if (act == '+'):
        res = a+b
    if (act == '-'):
        res = a-b
    if (act == '*'):
        res = a*b
    if (act == '/'):
        res = a/b
    return res

    
def main():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    act = str(input("Введите действие "))
    ans = calc(a,b,act)
    print(ans)
    pass
                                    
main()                                    