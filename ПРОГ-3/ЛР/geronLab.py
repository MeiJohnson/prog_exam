import math

def test_func(func, args):
  """
  Эта функция тестирует функцию Geron
  func - тестируемая функция,
  numCase - число случаев,
  args[0][0],args[0][1],args[0][2], args[0][3] - тестовые значения,
  args[0][4] - тип теста

  """
  if args[0][4] == 1:
    try:
      assert func(args[0][0],args[0][1],args[0][2]) == args[0][3]
    except:
      print('Тест на вычисление провален при a =',args[0][0],' b = ',args[0][1], 'c = ',args[0][2])
  elif args[0][4] == 2:
    try:
      assert type(func(args[0][0],args[0][1],args[0][2])) == float
    except:
      print('Тест на тип провален при a =',args[0][0],' b = ',args[0][1], 'c = ',args[0][2])
  print('Полученный ответ:', func(args[0][0],args[0][1],args[0][2]))

def geron(a,b,c):
  """Эта функция считает площадь треугольника по формуле Герона"""

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



if __name__ == '__main__':
  """
  assert type(geron(5,3,4)) is float, 'Ошибка, ответ не соответствует заданному типу'
  assert geron(10,6,8) == 24.0, 'Ошибка, неправильный ответ'

  assert geron(0,0,0) is not None, 'Ошибка, функция выводит неверное значение'

  try:
    assert geron(13.5,15,24.3) == 90.29399, 'Ошибка, неправильный ответ'
  except:
    print('Ошибка, неправильный ответ, при 13.5,15,24.3')
  try:
    assert geron(9.5,10,6) == 27.73415, 'Ошибка, неправильный ответ'
  except:
    print('Ошибка, неправильный ответ 9.5,10,6')
  """

  num_of_cases = int(input('Введите число тестовых случаев '))

  test_cases = []

  for el in range(num_of_cases):
    type_of_test = int(input('Введите тип проверки: 1 - сравнение ответов, 2 - сравнение типов '))
    f_val = float(input('Введите 1ое значение '))
    s_val = float(input('Введите 2ое значение '))
    th_val = float(input('Введите 3е значение '))
    test_val = float(input('Введите значение для сравнения '))
    temp_l = [f_val,s_val,th_val,test_val, type_of_test]
    test_cases.append(temp_l)

  test_func(geron, test_cases)
