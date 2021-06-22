"""
Разработать фрагмент программы, позволяющей получать данные
о текущих курсах валют с сайт ЦБ РФ с использованием сервиса,
который они предоставляют.
"""

import urllib.request
from xml.dom import minidom

def dailyCourse():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"

    page = urllib.request.urlopen(url) # открываем url
    data = page.read() # считываем его

    
    UrlSplit = url.split("/")[-1] # называем файл
    ExtSplit = UrlSplit.split(".")[1]
    fileName = UrlSplit.replace(ExtSplit, "xml") # добавляем расширение
    with open(fileName, "wb") as localFile: # записываем данные в файл
        localFile.write(data)
    
    page.close() # закрываем страничку

    doc = minidom.parse(fileName) # начинаем парсинг xml
    head = "Идентификатор; Номинал; Название валюты; Сокращение; Курс (руб) \n" # Название столбцов
    currency = doc.getElementsByTagName("Valute") # Получаем данные о валютах
    
    with open("exchange.txt","w") as out: # записываем в файл
        out.write(head)
    
        for rate in currency:
            sid = rate.getAttribute("ID")
            charcode = rate.getElementsByTagName("CharCode")[0]
            name = rate.getElementsByTagName("Name")[0]
            value = rate.getElementsByTagName("Value")[0]
            nominal = rate.getElementsByTagName("Nominal")[0]
            str = "{0}; {1}; {2}; {3}; {4} \n".format(sid,
            nominal.firstChild.data, 
            name.firstChild.data, charcode.firstChild.data, 
            value.firstChild.data)
            out.write(str)

dailyCourse()