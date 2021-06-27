import csv
import random
import statistics
import math

def csvGen():
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        # file_writer.writerow(["x", "y"])
        for n in range(100):
            file_writer.writerow([random.randint(0,101), random.randint(0,101)])
    pass
# csvGen()

def midVal(lst):
    summa = 0
    for el in lst:
        summa+=el
    return summa/len(lst)



def main():
    data_lst = []
    with open('data.csv') as File:  
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            data_lst.append(int(row[0])) 
    mVal = midVal(data_lst)

    var = statistics.variance(data_lst)
    print("Дисперсия",var)
    print("Среднее арифметическое",mVal)
    sqrt_var = math.sqrt(var)
    print("Среднеквадратичное отклонение",sqrt_var)

main()