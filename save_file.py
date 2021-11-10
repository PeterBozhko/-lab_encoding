def save(name, tree, data):
    f = open("name.bin", "wb")
    d = tree
    # |кол-во символов в дереве(8 бит)|длина кода для кодирования длины слова в битах(8 бит)|буква по ASCII (8 бит)|n бит - длина кода| сам код |
    # кол-во символов в дереве(8 бит)
    # print(len(d))
    out_1 = len(d).to_bytes(2, "big")
    # print("out_1", len(d))
    # длина кода в битах(16 бит)
    max_len = 0  # узнали максимальную длину кодового слова
    for el in d.values():
        if len(el) > max_len:
            max_len = len(el)
    # довели его до степени 2 (кол-во бит)
    step = 0
    while 2 ** step <= max_len:
        step += 1
    out_2 = step.to_bytes(1, "big")
    # print("out_2", step)
    out_string_3 = ""
    for i in d.keys():
        # print("###############", i)
        key = bin(i).replace("0b", "")
        key = '0' * (8 - len(key)) + key
        len_of_word = bin(len(d[i])).replace("0b", "")
        # print(len_of_word, len(d[i]))
        len_of_word = '0' * (step - len(len_of_word)) + len_of_word
        word = d[i]
        # print(key, len_of_word, word)
        out_string_3 += key + len_of_word + word
    while len(out_string_3) % 8 != 0:
        out_string_3 += '0'
    out_3 = int(out_string_3, 2).to_bytes(len(out_string_3) // 8, "big")
    # print("out_3", out_string_3, len(out_string_3))
    count = 0
    while len(data) % 8 != 0:
        count += 1
        data += '0'
    out_2_5 = count.to_bytes(1, "big")
    out_4 = int(data, 2).to_bytes(len(data) // 8, "big")
    # print("out_4 =", data)
    f.write(out_1)
    f.write(out_2)
    f.write(out_2_5)
    f.write(out_3)
    f.write(out_4)
    f.close()