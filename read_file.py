def read(name):
    f = open(name, "rb")
    all_inp = f.readlines()
    inp = all_inp[0]
    # print(all_inp)
    for i in range(1, len(all_inp)):
        inp += all_inp[i]
    # print("input", inp)
    ans = ""
    for i in inp:
        x = bin(i).replace("0b", "")
        x = '0' * (8 - len(x)) + x
        ans += x
    # print("and---------------------", ans)
    # print("and---------------------", len(ans))
    out_0_1 = int(ans[:8], 2)
    ans = ans[8:]
    out_0_2 = ""
    for i in range(out_0_1):
        ch = chr(int(ans[:8], 2))
        out_0_2 += ch
        ans = ans[8:]
    print("out_0_3", ans[:8])
    out_0_3 = int(ans[:8], 2)
    ans = ans[8:]
    out_0_4 = ans[:out_0_3*8]
    print("out_0_4_1", out_0_3,out_0_4)
    out_0_4 = int(out_0_4, 2)
    ans = ans[out_0_3*8:]
    print("out_0_4_2", out_0_4)

    out_1 = int(ans[:16], 2)
    out_2 = int(ans[16:24], 2)
    out_2_5 = int(ans[24:32], 2)
    # print("out", out_1, out_2, out_2_5)

    if out_2_5 != 0:
        ans = ans[32:-out_2_5]
    else:
        ans = ans[32:]
    d = dict()
    len_of_dict = 0
    # print("inp", ans)
    for i in range(out_1):
        key = int(ans[:8], 2)
        len_of_word = int(ans[8:8 + out_2], 2)
        word = ans[8 + out_2:8 + out_2 + len_of_word]
        ans = ans[8 + out_2 + len_of_word:]
        len_of_dict += 8 + out_2 + len_of_word
        d.update({key: word})
    # print(len_of_dict)
    if len_of_dict % 8 != 0:
        ans = ans[(8 - len_of_dict % 8):]

    # out_3 = bin(inp[2], )
    # out_3 = out_3[2:]
    # while len(out_3) != 8:
    #     out_3 = '0'+out_3
    # print(out_1, out_2, out_3)
    # for i in range(out_1):
    #     print(out_3[:out_2])
    #     out_3 = out_3[out_2:]

    f.close()
    return out_0_2, out_0_4, ans, d
