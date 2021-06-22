# для работы с файлами (в частности, для чтения) используется метод open

# откроем приложенный файл

handle = open('/home/vasya/Документы/Github/prog3/lab11/MOCKDATA.json')

# по умолчанию он будет открыт для чтения, что нам и необходимо

print(handle)
# > <_io.TextIOWrapper name='MOCK_DATA.json' mode='r' encoding='UTF-8'>
# для чтения мы используем метод readlines() объекта handle, который мы получили ранее

lines = handle.readlines()

# readlines() считывает весь файл от начала и до конца.

# print(lines)
# будет выведено всё содержимое файла
# ['[{"id":1,"first_name":"Susann","last_name":"Wyldish","email":"swyldish0@bing.com","gender":"Female","ip_address":"112.109.35.15"},\n', '{"id":2,"first_name":"Oliy","last_name":"Bruton", ...
# ... ,"ip_address":"45.97.107.40"}]']

# таким образом, нам необходимо итерироваться по считанному содержимому и поместить поля, которые мы собираемся записать в csv в какую-то структуру

# итерироваться по cчитанному файлу можно с помощью цикла for ... in ...
for line in lines:
    pass
    # print(line)

# будут выведены строчки из файла

# теперь нам необходимо с помощью строковых методов получить ключи (например, id, first_name, last_name, ...) и их значения (1, Susann, Wyldish, ...)
# Вопрос 1:
# какие строковые функции могут быть для этого использованы?
id_list = []
what = "gender"
for line in lines:
    #print(line.find("id"))
    #pass
   
    if line.find(what):
        temp2 = line.find(what)+len(what)+2
        temp = line.find(",",temp2,len(line)-1)
        ss = line[temp2:temp]
        ss2 = ss.replace("\"","")
        id_list.append({what:ss2})

# print(id_list)

# Как только мы считаем значения их имеет смысл положить в какую-нибудь структуру данных

# Вопрос 2
# Какую структуру для этого можно использовать?
# Словарь?
# Таким образом мы сформируем объект, который требуется записать в csv формат.

# Файл в конце работы с ним требуется закрыть
handle.close()

# Рассмотрим теперь как работать с csv-файлами.
# Работа с csv осуществляется с помощью специального модуля
# Официальная документация по этому модулю по ссылке: https://docs.python.org/3/library/csv.html

# В документации есть хороший пример с демонстрацией записи в csv файл:

import csv
import json

with open('MOCKDATA.json') as f:
    data_dict = json.load(f)
print(data_dict[0]['first_name'])
print(data_dict[0].values())

with open('eggs.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    jsonwriter.writerow(data_dict[0].keys())
    keys = data_dict[0].keys()
    for el in data_dict:
        jsonwriter.writerow(el.values())

