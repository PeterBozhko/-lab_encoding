import Coder
import Decoder
import main

arr_names = ["bib", "book1", "book2", "geo", "news", "obj1", "obj2", "paper1", "paper2", "pic", "progc", "progl",
             "progp", "trans"]
for i in arr_names:
    # Coder.encode("calgarycorpus/" + i, "calgarycorpus/" + i +"_d")
    # Decoder.decode("calgarycorpus/" + i +"_d", "calgarycorpus/" + i +"_e")
    main.calc_H("calgarycorpus/" + i)
