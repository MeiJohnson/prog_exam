 
"""
Царулкова Анастасия
группа 2 подгруппа 3

Задание 2.2 ВСР

Здесь представлена программа, которая для заданного количества значений возвращала бы
список из уникальных элементов, содержащихся во входном наборе значений, 
c использованием упаковки и распаковки элементов.
"""

def unique(*args):
  lst = []
  lst.append(args[0])
  for el in range(len(args)):
    if args[el] in lst:
      pass
    else:
      lst.append(args[el])
  return lst

def main():
  result = unique(1,4,5,6,5,'7','5','7')
  print(result)
 
main()