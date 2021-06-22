

def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, по которой мы ищем: ")

    change_str = input("Введите строку для замены: ")
    
    choice = None
    while choice != '4':

        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')

        print('3 - найти все вхождения подстроки' )

        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        
        if choice == '1':
            search_str(input_str, searchable_str)
             

        if choice == '2':
            pass
            # найти функцию, позволяющую осуществлять замену подстроки строкой

        if choice == '3':
            search_n_replace_str(input_str,change_str,searchable_str)


def search_str(what="", where=""):
    # 1 - поиск первого вхождения подстроки
    flag = False
    i = 0
    while i < len(where):
        if i+len(what)-1 < len(where) and where[i:i+len(what)] == what:
           flag = True
           index = i
           i = len(where)-1   
        i+=1
    if flag == True:
        print("Начало ",index, " - Нашел")
    else:
        print("Не нашел")



def search_n_replace_str(what="",  to_what="", where=""):
    # what - что меняем
    # to_what - на что меняем
    # where - где меняем
    # 3 - найти все вхождения подстроки
    
    i = 0
    while i < len(where):
        if i+len(what)-1 < len(where) and where[i:i+len(what)] == what:
            start = where[0:i]
            end = where[i+len(what):len(where)]
            start +=to_what + end
            where = start
            i+=len(what)-1
        i+=1 
    print(where)
    




main()