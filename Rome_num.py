def conv_rom_to_arab(num):
    rome_dig = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    new = 0
    pr_value = 0
    # Чтение числа справа налево, чтобы понять складывать или вычитать число
    for char in reversed(num):
        value = rome_dig[char]
        if value >= pr_value:
            new += value
        else:
            new -= value
        pr_value = value
    return new








def conv_arab_to_rom(num):
    # Пишем всевозможные комбинации, чтобы избежать повтора символов более 3 раз
    rome_dig = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    new = ""
    # Чтение числа справа налево, чтобы записывать первыми значения старших разрядов
    for char, value in reversed(rome_dig.items()):
        while value <= num:
            new += char
            num -= value
    return new

num = int(input("Введите арабское число: ").strip())
print(conv_arab_to_rom(num))

num = input("Введите римское число: ").strip()
print(conv_rom_to_arab(num))

