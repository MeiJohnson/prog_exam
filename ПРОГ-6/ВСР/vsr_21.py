"""
Подсчет слов в тексте и длины каждого слова с выводом с помощью генератора.
"""

def word_counter(text):

    word_lst = text.split()
    yield len(word_lst)
    for el in word_lst:
        yield len(el)

g = word_counter("text text text text text text text text")
for i in g:
    print(i)

    

