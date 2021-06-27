def converter(num, to_type=None):
    if (num >=0 and num <= 9):
        num_names=[
            "Нуль",
            "Один",
            "Два",
            "Три",
            "Четыре",
            "Пять",
            "Шесть",
            "Семь",
            "Восемь",
            "Девять"
        ]
        print(num_names[num])
        if (to_type == 'bin'):
            print(bin(num))
        if (to_type == 'oct'):
            print(oct(num))
        if (to_type == 'hex'): 
            print(hex(num))
    else:
        print("Введите число от 0 до 9 включительно")

converter(9)
converter(3, "hex")
converter(16)