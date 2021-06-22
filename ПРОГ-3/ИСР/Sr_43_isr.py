
"""
Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран.
Организовать тестирование работоспособности программы с помощью assert, print.
"""
import pytest
import json

def json_table(data):

    table = []
    sstr = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
    t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id','first_name','last_name','email','gender','ip_address')
    roof = '-'*len(t_caption)
  
    table.append(roof)  
    table.append(t_caption)
    table.append(roof)  

    for el in range(len(data)):
        temp = data[el]
        res = sstr.format(**temp)
        table.append(res)
    table.append(roof)
    
    return(table)

def main():
    with open('MOCKDATA.json') as f:
        data_dict = json.load(f)
    a = json_table(data_dict)
    """
    for el in table:
    print(el)
    """
def test_json_table():
    assert json_table([{"id":1,"first_name":"Susann","last_name":"Wyldish","email":"swyldish0@bing.com","gender":"Female","ip_address":"112.109.35.15"},
    {"id":2,"first_name":"Oliy","last_name":"Bruton","email":"obruton1@forbes.com","gender":"Female","ip_address":"166.20.188.54"},
    {"id":3,"first_name":"Ginelle","last_name":"Inkpen","email":"ginkpen2@tinypic.com","gender":"Female","ip_address":"208.129.167.239"}]) == ['---------------------------------------------------------------------------------------------------',
'| id  | first_name |    last_name    |             email              | gender |    ip_address    |',
'---------------------------------------------------------------------------------------------------',
'|  1  |   Susann   |     Wyldish     |       swyldish0@bing.com       | Female |  112.109.35.15   |',
'|  2  |    Oliy    |     Bruton      |      obruton1@forbes.com       | Female |  166.20.188.54   |',
'|  3  |  Ginelle   |     Inkpen      |      ginkpen2@tinypic.com      | Female | 208.129.167.239  |',
'---------------------------------------------------------------------------------------------------']

if __name__ == "__main__":
    main()