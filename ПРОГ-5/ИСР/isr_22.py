"""
Создание программы, возвращающей список чисел 
Фибоначчи с помощью итератора.

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
    
    maxi = int(input('Введите максимальное значение '))
    res = fib(maxi)
    for x in res:
        print(x)
    pass

main()