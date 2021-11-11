import read_file
import huffman
import mtf
import bwt


def save_orig(name, int_array):
    f = open(name, "wb")
    [f.write(i.to_bytes(1, "big")) for i in int_array]
    f.close()


def decode(name_of_file, restore_name):
    num, enc, tree_dict = read_file.read(name_of_file)
    tree = huffman.calc_tree(tree_dict)
    before_mtf_decoder = huffman.Huffman_Decoding(enc, tree[0])
    before_bwt_decoder = mtf.mtf_decoder(before_mtf_decoder)
    answer_string = bwt.bwt_decoder_smart(before_bwt_decoder, num)
    save_orig(restore_name, answer_string)
    print("Done")
