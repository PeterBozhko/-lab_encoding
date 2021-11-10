def mtf_encode(st):  # преобразование методом "стопки книг" (Move-To-Front, MTF)
    init_alphabet = sorted(list(set(st)))  # берём алфавит
    alphabet = init_alphabet.copy()
    answer = []
    for el in st:
        # print("alphabet", st, alphabet, el)
        num = alphabet.index(el)  # индекс элемента строки в алфавите
        answer.append(num)  # добавляем к ответу
        alphabet.pop(num)
        alphabet.insert(0, el)  # изменение алфавита
    return answer, init_alphabet


def mtf_decoder(array, alphabet):  # обратное преобразование методом "стопки книг" (Move-To-Front, MTF)
    # answer = ""
    answer_array = []
    for el in array:
        index = int(el)
        # al = alphabet.index(el)
        element = alphabet[index]
        # answer += element  # добавляем к ответу элемент алфавита по индексу
        answer_array.append(element)
        alphabet.pop(index)
        alphabet.insert(0, element)  # изменяем алфавит также как при кодировании
    # return answer
    return answer_array
