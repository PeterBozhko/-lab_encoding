import bwt
import mtf
import huffman
import save_file


def coder(name_of_file):
    fin = open(name_of_file, "rb")
    data = list(map(int, fin.read()))
    fin.close()
    data, num = bwt.new_bwt(data)
    print("bwt_encode_result :", num, data)
    bwt_encode_result = data
    data, init_alp = mtf.mtf_encode(data)
    mtf_encode_result = ""
    for i in data:
        mtf_encode_result += str(i)
    # print("mtf_encode_result :", mtf_encode_result)
    huffman_code, tree = huffman.huffman_encoder(data)
    # print("huffman_code", huffman_code)
    # ----------------------------------SAVING----------------------------------
    save_file.save(name_of_file, num, huffman.calc_code(tree), huffman_code)
