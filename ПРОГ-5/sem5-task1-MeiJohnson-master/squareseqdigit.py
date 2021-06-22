
def squareSequenceDigit(n):
    step = 0 # начальная позиция
    i = 0
    while step < n:
       i += 1
       p = i*i
       pos = 1 # позиция в квадрате числа
       div = 10 # делитель
       
       while (p // div != 0): # считаем цифры
            div *= 10
            pos+=1
       step+=pos
    
    step -= pos # возврат к предыдущему числу
    div //= 10

    while (step != n): # продолжаем искать
        result = p // div % 10
        div //= 10
        step+=1 # доходим до нужной цифры
    return result


print(squareSequenceDigit(27))
    
    
    
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)
    
