"""
1.2. Дополнение программы для считывания данных проверкой 
утверждений или высказываний (assert). Создание отдельного 
блока для такой проверки (с помощью __name__) и скрипта командной 
строки для запуска этих проверок.
"""

import json

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
    
    return(table)

def main():
    a = json_table('MOCKDATA.json')
    print(type(a))
    for el in a:
        print(el)
  
if __name__ == "__main__":
    assert type(json_table('MOCKDATA.json')) == list, "Типы не совпадают" 
    assert type(json_table('MOCKDATA.json')) != tuple

main()    