#Угадай число
import random

random.seed(version=2)

flag = False
start = int(input("Введите начало интервала "))
end = int(input("Введите конец интервала "))
guess_num = random.randint(start,end)

while flag != True:
    num = int(input("Введите предполагаемое число"))
    s = "Ваше число {}.".format(num)
    print(s)
    
    if guess_num == num:
        print("Вы угадали. Поздравляю!")
        flag = True
    else:
        print("Вы не угадали.")
