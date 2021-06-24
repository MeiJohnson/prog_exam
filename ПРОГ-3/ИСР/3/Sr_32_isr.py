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

def main():
    input_str = input("Введите строку для поиска: ")
    searchable_str = input("Введите строку, по которой мы ищем: ")
    search_str(input_str, searchable_str)

main()