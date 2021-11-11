import bwt
import mtf
import huffman
import save_file


def encode(name_of_input_file, name_of_output_file):
    fin = open(name_of_input_file, "rb")
    data = list(map(int, fin.read()))
    fin.close()
    data, num = bwt.new_bwt(data)
    data = mtf.mtf_encode(data)
    mtf_encode_result = ""
    for i in data:
        mtf_encode_result += str(i)
    huffman_code, tree = huffman.huffman_encoder(data)
    save_file.save(name_of_output_file, num, huffman.calc_code(tree), huffman_code)
    print("Done")
