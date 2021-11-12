import math
import copy

alp = 256


def h_x(data):
    freq = {}
    for i in range(alp):
        freq.update({i: 0})
    for i in data:
        freq[i] += 1
    n = len(data)
    answer = 0
    for i in range(len(freq)):
        if freq[i] == 0:
            continue
        answer -= (freq[i] / n * math.log2(freq[i] / n))
    return answer


def h_x_x(data):
    freq = {}
    for i in range(alp):
        freq.update({i: 0})
    freq_2 = {}
    for i in range(alp):
        freq_2.update({i: freq.copy()})

    for i in data:
        freq[i] += 1

    for i in range(len(data) - 1):
        freq_2[data[i]][data[i + 1]] += 1
    n = len(data)

    answer = 0
    for i in range(alp):
        if freq[i] == 0:
            continue
        for j in range(alp):
            if freq[j] == 0 or freq_2[i][j] == 0: continue
            p_x = freq_2[i][j] / n
            p_x_x = freq_2[i][j] / freq[j]
            answer -= (p_x * math.log2(p_x_x))
    return answer


def h_x_xx(data):
    freq = {}
    for i in range(alp):
        freq.update({i: 0})
    freq_2 = {}
    for i in range(alp):
        freq_2.update({i: copy.deepcopy(freq)})
    freq_3 = {}
    for i in range(alp):
        freq_3.update({i: copy.deepcopy(freq_2)})

    for i in data:
        freq[i] += 1

    for i in range(len(data) - 1):
        freq_2[data[i]][data[i + 1]] += 1

    for i in range(len(data) - 2):
        freq_3[data[i]][data[i + 1]][data[i + 2]] += 1
    n = len(data)

    answer = 0
    for i in range(alp):
        if freq[i] == 0:
            continue
        for k in range(alp):
            if freq[k] == 0:
                continue
            for j in range(alp):
                if freq_3[i][k][j] == 0 or freq_2[i][k] == 0: continue
                p_2 = freq_3[i][k][j] / freq_2[i][k]
                p_1 = (freq_2[i][k] / n) * p_2
                answer -= (p_1 * math.log2(p_2))
    return answer


def calc_H(name):
    fin = open(name, "rb")
    data = list(map(int, fin.read()))
    fin.close()
    h1 = h_x(data)
    h2 = h_x_x(data)
    h3 = h_x_xx(data)
    print(name, ": H(X) :", h1, "H(X|X) :", h2, "H(X|XX)", h3)
