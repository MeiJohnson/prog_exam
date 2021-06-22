import csv
import matplotlib.pyplot as plt
import pandas as p
import numpy as np

with open('prices.csv',encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Имена столбцов {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tКвартира за {row[0]} рублей находится в {row[1]}.')

data=np.genfromtxt('prices.csv', delimiter=';',skip_header=1, names=['Цена', 'Район'], dtype=None, encoding=None)
fig, ax1 = plt.subplots()
print(data['Цена'],data['Район'])
ax1.scatter(x=data['Цена'],y=data['Район'],color='b',label='Цены на недвижимость')
plt.xlabel("Цены")
plt.ylabel("Районы")
plt.show()