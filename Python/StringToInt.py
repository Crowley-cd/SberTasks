# Transformate string's nubmers to Int

###
# Не стал удалять неиспользуемые функции, для того, чтобы в будущем можно было
# дополнить функциональность программы.
# Функции load, enter, add работают с файлом nums.txt

# Для удобства запуск на других устройствах перенес словарь из внешних файлов в код.
###

import os

nums = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
    'семь': 7, 'восемь': 8, 'девять': 9,
    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
    'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17,
    'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30,
    'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
    'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200,
    'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600,
    'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900, 'тысяча': 1000,
    'тысячи': 1000, 'тысяч': 1000, 'миллион': 1000000
}
inp = None


def load():
    with open('nums.txt', 'r') as load:
        try:
            for string in load.readlines():
                if string == 'exit':
                    continue
                string = string.rstrip()
                k, v = string.split(':')
                nums[k] = int(v)
        except ValueError:
            pass


def enter():
    with open('nums.txt', 'w') as file:
        while inp != 'exit':
            inp = input()
            file.write(inp + '\n')
        main_menu()


def add():
    inp = None
    with open('nums.txt', 'a') as added:
        while inp != 'exit':
            inp = input()
            added.writelines(inp + '\n')
        main_menu()


def str_to_int():
    sum = 0

    input_str = input("Введите число:").lower() # Читаем строку и избавляемся от различий регистра

    if 'тысяч' not in input_str:
        for st in input_str.split(' '):
            sum += nums[st]
    else:
        th, de = input_str.split('тысяч')
        for t in th.split(' '):  # игнорируем артефакты (strip может заменить)
            if t == ' ' or t == '':
                continue
            sum += nums[t]

        sum *= 1000

        for d in de.split(' '):
            if d == 'и' or d == 'a' or d == '':  # игнорируем окончания(тысячА)
                continue
            sum += nums[d]

    return print(sum)


def main_menu():
    print('Enter programm mode:')
    print('load, enter, add, transform, exit')
    print('by default - load -> transform')

    on = input()

    if on == 'load':
        load()
    elif on == 'enter':
        enter()
    elif on == 'add':
        add()
    elif on == 'exit':
        exit(1)
    else:
        load()
        str_to_int()


# main_menu()
str_to_int()