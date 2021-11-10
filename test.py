import bwt
init_string = [97, 98, 114, 99, 97, 100]
# init_string = 'abrac'
# for i in range(len(init_string)):
#     init_string[i] = chr(init_string[i])
encode, num = bwt.bwt_encoder(init_string)
print(encode, num)
answer = bwt.bwt_decoder_smart(encode, num)
print("init", init_string)
print("answ",answer)
print(answer == init_string)
