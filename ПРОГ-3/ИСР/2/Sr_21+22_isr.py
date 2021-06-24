"""
Царулкова Анастасия Витальевна
2 группа 3 подгруппа

Copyright: 10.2019

Задание 2.1 + 2.2 ИСР
Cкрипт с функцией, которая строит таблицу истинности для логического выражения.

"""


def logic_values(l, *args):
    return int(l(*args))


def printHeader(*args):
    result = ''
    lst_of_len = []
    for el in args:
        lst_of_len.append(len(str(el))+2)
    lst_of_result = []
    for el in range(len(lst_of_len)):
        lst_of_result.append(str(args[el]).center(lst_of_len[el]))

    for el in range(len(lst_of_result)):
        result += '|'+lst_of_result[el]
    result += '|'
    row_length = len(result)
    print('-'*row_length)
    print(result)
    return lst_of_len


def printRow(lst, *args):
    result = ''
    lst_of_result = []
    for el in range(len(lst)):
        lst_of_result.append(str(args[el]).center(lst[el]))

    for el in range(len(lst_of_result)):
        result += '|'+lst_of_result[el]
    result += '|'
    row_length = len(result)
    print('-'*row_length)
    print(result)


def main():
    A = [0, 0, 0, 0, 1, 1, 1, 1]
    B = [0, 0, 1, 1, 0, 0, 1, 1]
    C = [0, 1, 0, 1, 0, 1, 0, 1]

    temp_list = printHeader('A', 'B', 'C', '¬C', 'A ˄ B', 'B ˄ C',
                            '¬C → A', 'A ˄ B ↔ B ˄ C', '(A ˄ B ↔ B ˄ C) ˅ (¬C -> A)')

    for el in range(len(A)):
        ans1 = logic_values(lambda c: not c, C[el])
        ans2 = logic_values(lambda a, b: a and b, A[el], B[el])
        ans3 = logic_values(lambda b, c: b and c, B[el], C[el])
        ans4 = logic_values(lambda c, a: c or a, ans1, A[el])
        ans5 = logic_values(lambda a, b: a == b, ans2, ans3)
        ans6 = logic_values(lambda a, b: a or b, ans5, ans4)
        printRow(temp_list, A[el], B[el], C[el],
                 ans1, ans2, ans3, ans4, ans5, ans6)
