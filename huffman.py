codes = dict()
# Лист дерева Хаффмана
class Node:
    def __init__(self, count, symbol, left=None, right=None):
        self.symbol = symbol  # символ
        self.count = count  # количество символов в строке
        self.left = left  # левый ребенок
        self.right = right  # правый ребенок
        self.code = ''  # направление дерева 0 или 1


def calc_count(data):
    symbols = dict()
    for el in data:
        if symbols.get(el) is None:
            symbols[el] = 1
        else:
            symbols[el] += 1
    return symbols


def calc_tree(d):
    new_nodes = []
    new_nodes.append(Node(None, None))
    for el in d.keys():
        word = d[el]
        i = 0
        curr_node = new_nodes[0]
        while len(word) > 1:
            if word[0] == '0':
                if curr_node.left is None:
                    curr_node.left = Node(None, None)
                    curr_node.left.code = 0
                curr_node = curr_node.left
            if word[0] == '1':
                if curr_node.right is None:
                    curr_node.right = Node(None, None)
                    curr_node.right.code = 1
                curr_node = curr_node.right
            word = word[1:]
        if word == '0':
            curr_node.left = Node(None, el)
            curr_node.left.code = 0
        if word == '1':
            curr_node.right = Node(None, el)
            curr_node.right.code = 1
    return new_nodes


def calc_code(node, val=''):  # рекурсивная функция поиска кодов Хаффмана по дереву
    new_val = val + str(node.code)
    if node.left:
        calc_code(node.left, new_val)
    if node.right:
        calc_code(node.right, new_val)
    if not node.left and not node.right:
        codes[node.symbol] = new_val
    return codes


def Total_Gain(data, coding):
    before_compression = len(data) * 8  # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])  # calculate how many bit is required for that symbol in total
    # print("Space usage before compression (in bits) :", before_compression)
    # print("Space usage after compression (in bits) :", after_compression)


def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        #  print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def huffman_encoder(data):  # кодирование алгоритмом Хаффмана
    symbol_with_probs = calc_count(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    # print("symbols: ", symbols)
    # print("probabilities: ", probabilities)

    nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.count)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.count + right.count, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calc_code(nodes[0])
    # print("symbols with codes :", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    return encoded_output, nodes[0]


def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    return decoded_output