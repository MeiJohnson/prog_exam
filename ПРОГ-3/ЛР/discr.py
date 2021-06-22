import math

"""
def discr(b,a,c=-4):
    print(a,b,c)
    \"""
        Вычисление дискримнанта

        Расширенное описание
        - Входные и выходные значения
        - особенности функции
        - что она возвращает и т. д.
    \"""
    # docstring
    return b*b-4*a*c

a = int(input("Введите а "))
b = int(input("Введите b "))
c = int(input("Введите с "))

print(discr(b,a,c))

print(discr.__doc__)
# упаковка распаковка позиционных аргументов функции.
#Упакованы они будут в кортеж, тк они не должны изменятся

discr(*[1,2,3])#распаковка

def sup_dis(*args): #упаковка
    print(args)

print(type(sup_dis(1,2,3)))
discr(*(1,2,3))#распаковка
"""
# упаковка распаковка ключевых аргументов функции.
#Упакованы они будут в словарь

def sup_sup_dis(a=None, b=None, c=None):
    print(a,b,c)

sup_sup_dis(**{'a':1,'b':2,'c':3})

def sup_sup_dis2(**kwargs):
    print(kwargs)
sup_sup_dis2(a=1,b=2,c=3,nick='molodec')
