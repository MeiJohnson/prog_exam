import math

def geron(a,b,c):
    """
    Царулкова Анастасия Витальевна
    2 группа 3 подгруппа
  
    Эта функция считает площадь треугольника по формуле Герона
    """ 
    p = 0.5*(a+b+c)
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return round(s,5)

def main():
    a = float(input("Введите а "))
    b = float(input("Введите b "))
    c = float(input("Введите с "))

    assert a + b > c and a + c > b and b + c > a, 'Ошибка, треугольник не существует'

    ans = geron(a,b,c)
    print(type(ans))
    print(ans)

main()
