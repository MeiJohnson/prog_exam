
"""
Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран.
Организовать тестирование работоспособности программы с помощью assert, print.
"""

import json

def json_table():
    """
    >>> json_table()[1]
    '| id  | first_name |    last_name    |             email             | gender |    ip_address    |'

    """

    with open('MOCKDATA.json') as f:
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
    
    return(table)

def main():
    a = json_table()
    """
    for el in table:
    print(el)
    """
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()