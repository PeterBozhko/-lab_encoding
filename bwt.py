import functools as ft


def cmp_str(a, b, st):
    for k in range(len(st)):
        # key = ord(st[a]) - ord(st[b])
        key = st[a] - st[b]
        a = (a + 1) % len(st)
        b = (b + 1) % len(st)
        if key != 0: return key
    return key


def new_bwt(data):
    shifts = [i for i in range(len(data))]
    ft.cmp_to_key(lambda x, y: cmp_str(x, y, data))
    shifts.sort(key=ft.cmp_to_key(lambda x, y: cmp_str(x, y, data)))
    # answer = ""
    answer_array = []
    print(shifts)
    for i in shifts:
        # answer += data[i - 1]
        answer_array.append(data[i - 1])
    # return answer, shifts.index(0)
    return answer_array, shifts.index(0)


def bwt_encoder(st):  # преобразование Барроуза — Уилера (BWT)
    array_of_rotations = sorted(st[i:] + st[:i] for i in range(len(st)))  # все возможные повороты строки
    number_of_init = array_of_rotations.index(st)  # индекс оригинальной строки
    output_string = [el[-1] for el in array_of_rotations]  # последний столбец
    return output_string, number_of_init


# def bwt_decoder_smart(st, number):  # обратное преобразование Барроуза — Уилера (BWT)
#     last_row = list(st.strip())  # разиваем строку на символы
#     first_row = last_row.copy()
#     first_row.sort()  # берём отсортированную строку
#     pairs = []
#     for i in range(len(last_row)):  # составляем пары: пара символов (последний + первый) + номер строки
#         pairs.append((last_row[i] + first_row[i], i))
#     pairs.sort()  # находим матрицу переходов
#     current = pairs[number][1]
#     answer = ""
#     for i in range(len(last_row)):  # составляем исходную строку
#         answer += last_row[current]
#         current = pairs[current][1]
#     return answer
def bwt_decoder_smart(array, number):  # обратное преобразование Барроуза — Уилера (BWT)
    last_row = array  # разиваем строку на символы
    first_row = last_row.copy()
    first_row.sort()  # берём отсортированную строку
    pairs = []
    for i in range(len(last_row)):  # составляем пары: пара символов (последний + первый) + номер строки
        pairs.append((chr(last_row[i]) + chr(first_row[i]), i))
    pairs.sort()  # находим матрицу переходов
    current = pairs[number][1]
    answer_array = []
    for i in range(len(last_row)):  # составляем исходную строку
        answer_array.append(last_row[current])
        current = pairs[current][1]
    # return answer
    return answer_array

def bwt_decoder_smart_smart(array, number):  # обратное преобразование Барроуза — Уилера (BWT)
    indices = [i for i in range(len(array))]
    indices.sort(key=ft.cmp_to_key(lambda x, y: cmp_str(x, y, array)))
    answer_array = []
    current = indices[number]
    print("indices", indices)
    # while (current != number):
    print(array)
    for i in range(len(array)):  # составляем исходную строку
        print("current", current)
        answer_array.append(array[current])
        current = indices[current]
    return answer_array
#[97, 98, 114, 97, 100, 97, 98, 114, 97, 98, 114]