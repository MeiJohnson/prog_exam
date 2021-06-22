# ROT13
import string
alphabet_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_up = "АБВГДЕЁЖЗИЙКДМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def rot13(s):
    new_s = ""
    for char in s:
        if char in string.ascii_lowercase:
            if string.ascii_lowercase.find(char)+13 < len(string.ascii_lowercase):
                new_s += string.ascii_lowercase[string.ascii_lowercase.find(char)+13]
            else:
                add = abs(len(string.ascii_lowercase)-string.ascii_lowercase.find(char)-13)
                new_s += string.ascii_lowercase[add]
        elif char in string.ascii_uppercase:
            if string.ascii_uppercase.find(char)+13 < len(string.ascii_uppercase):
                new_s += string.ascii_uppercase[string.ascii_uppercase.find(char)+13]
            else:
                add = abs(len(string.ascii_uppercase)-string.ascii_uppercase.find(char)-13)
                new_s += string.ascii_uppercase[add]
        elif char in alphabet_low:
            if alphabet_low.find(char)+13 < len(alphabet_low):
                new_s += alphabet_low[alphabet_low.find(char)+13]
            else:
                add = abs(len(alphabet_low)-alphabet_low.find(char)-13)
                new_s += alphabet_low[add]
        elif char in alphabet_up:
            if alphabet_up.find(char)+13 < len(alphabet_up):
                new_s += alphabet_up[alphabet_up.find(char)+13]
            else:
                add = abs(len(alphabet_up)-alphabet_up.find(char)-13)
                new_s += alphabet_up[add]
        else:
            new_s+=char
    print(new_s)

def main():
    s = str(input("Введите строку для шифрования:"))
    rot13(s)

main()