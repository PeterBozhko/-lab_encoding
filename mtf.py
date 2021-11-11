def mtf_encode(st):  # преобразование методом "стопки книг" (Move-To-Front, MTF)
    alphabet = [i for i in range(256)]  # берём алфавит [0,255]
    answer = []
    for el in st:
        num = alphabet.index(el)  # индекс элемента строки в алфавите
        answer.append(num)  # добавляем к ответу
        alphabet.pop(num)
        alphabet.insert(0, el)  # изменение алфавита
    return answer


def mtf_decoder(array):  # обратное преобразование методом "стопки книг" (Move-To-Front, MTF)
    alphabet = [i for i in range(256)]
    answer_array = []
    for el in array:
        index = int(el)
        element = alphabet[index]
        answer_array.append(element)
        alphabet.pop(index)
        alphabet.insert(0, element)  # изменяем алфавит также как при кодировании
    return answer_array
