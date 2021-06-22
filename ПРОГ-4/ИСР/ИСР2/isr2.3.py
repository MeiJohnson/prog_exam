import functools

def deco(func):
    @functools.wraps(func)
    def wrap(*args):
        f = open('a.out', 'w')
        #print("Смотри, что я получил:", args[0], args[1], args[2])
        result = func(*args)
        name = ''
        if (args[2] == '+'):
            name = 'Сложение'
        elif (args[2] == '-'):
            name = 'Вычитание'
        elif (args[2] == '*'):
            name = 'Умножение'
        elif (args[2] == '/'):
            name = 'Деление'
        else:
          return "Неизвестное действие"
        f.write(f"{args[0]}, {args[1]}, {name}, {result}")
        f.close()
        return result
    return wrap

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
    v = deco(calc)
    
    ans = v(a,b,act)
    print(ans)
    pass
                                    
main()                                    
