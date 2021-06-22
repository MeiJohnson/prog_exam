"""
Разработать программу с реализацией функции для считывания 
json-данных из файла и вывод их в табличном виде на экран. 
Реализовать базовый синтаксис для обработки исключений (try .. except)
"""
import json

try:
    with open('MOCKDATAS.json') as f:
        data_dict = json.load(f)
except FileNotFoundError as e:
    print(e)

try:
    with open('MOCKDATA.json') as f:
        data_dict = json.load(r)
except NameError as e:
    print(e)

try:
   for el in range(len(data_dict)):
        temp = data_dit[el]
        res = sstr.format(**temp)
        table.append(res)
except NameError as e:
    print(e)

def json_table(fl):
  

    with open(fl) as f:
        data_dict = json.load(f)

    table = []
    sstr = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
    t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id','first_name','last_name','email','gender','ip_address')
    roof = '-'*len(t_caption)
  
    table.append(roof)  
    table.append(t_caption)
    table.append(roof)  

    for el in range(len(data_dict)):
        temp = data_dict[el]
        res = sstr.format(**temp)
        table.append(res)
    table.append(roof)
    
    return table

def main():
    a = json_table('MOCKDATA.json')
    for el in a:
        print(el)


main()

