# Test task from Sber (Two letter)

def two_letter(strg: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyza'
    tl_status = True
    while tl_status:
        for num_letter in range(len(alphabet)):
            if strg.count(alphabet[num_letter]) >= 2:
                tl_status = True
                if alphabet[num_letter] * 2 in strg:  # Второе условие реализует функционал первого,
                                                     # но первое может сократить время на выполнение
                    strg = strg.replace(alphabet[num_letter] * 2, alphabet[num_letter + 1])  # Если две буквы находятся
                    print(strg)                                                              # рядом
                    return two_letter(strg)
                else:
                    for i in range(len(strg)):                                           # Если буквы разбросаны по
                        if strg[i] == alphabet[num_letter]:                              # строке.
                            save_position = i
                            strg = list(strg)
                            strg[save_position] = alphabet[num_letter + 1]
                            strg = ''.join(strg)
                            strg = strg.replace(alphabet[num_letter], '', 2)
                            print(strg)
                            return two_letter(strg)
                print(strg)
            else:
                tl_status = False
    return print('result: ', strg)


def rem_two_letter(string: str, letter: str):  # Вынесенная функция для упрощения будущей модернизации
    string = string.replace(letter, '', 2)
    return string


strng = input()
two_letter(strng)
