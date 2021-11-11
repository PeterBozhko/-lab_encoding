import Coder
import Decoder

# Coder.encode("main.py", "encoded_main2")
# Decoder.decode("encoded_main2", "main.py")
import sys
print(sys.argv)
if len(sys.argv) == 4:
    if sys.argv[1] == "-e":
        Coder.encode(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-d":
        Decoder.decode(sys.argv[2], sys.argv[3])
    else:
        print("incorrect arguments")
else:
    print("incorrect arguments")