import random
def main():
    """
    Создание программы по распределению списка с 
    случайными значениями на два списка по определенному 
    критерию (четность/нечетность, положительные/отрицательные числа).
    """
    N = int(input("Введите размер массива "))
    lst = [random.randint(-10,10) for i in range(N)]
    print(lst)
    crit = str(input("Введите критерий разделения массива (чет/знак)"))
    
    print(lst)
    if(crit == "чет"):
        lst.sort()    
        lst.sort(key = lambda x: x % 2,reverse=False)
        print(lst)
        # print(len(lst)/2)
        x = min(lst)
        print(lst.index(x))
        if lst.index(x)!=0:
            res1 = lst[:lst.index(x):]
            res2 = lst[lst.index(x)::]
            print(res1)
            print(res2)
        else:
            lst.sort(key = lambda x: x % 2, reverse=True)
            x = min(lst)
            res1 = lst[:lst.index(x):]
            res1.sort()
            res2 = lst[lst.index(x)::]
            res2.sort()
            print(res1)
            print(res2)
    if(crit == "знак"):
        res1 = []
        res2 = []
        for i in range(len(lst)):
            if (lst[i] < 0):
                res1.append(lst[i])
            else:
                res2.append(lst[i])
        print(res1)
        print(res2)
        
main()