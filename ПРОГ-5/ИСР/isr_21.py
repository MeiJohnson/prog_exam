"""
Разработать функцию, возвращающую элементы ряда 
Фибоначчи по данному максимальному значению.

(с) Царулкова А.В.
"""

def fib(maximum):
    prev = 1
    cur = 1
    resLst = [prev, cur]
    
    while(prev < maximum):
        tmp = prev + cur
        prev = cur
        cur = tmp
        if (cur < maximum):
            resLst.append(cur)

    return resLst

def main():
    
    max = int(input('Введите максимальное значение '))
    print(fib(max))
    pass

main()