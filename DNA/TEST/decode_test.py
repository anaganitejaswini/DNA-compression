from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import json
import binascii

def huffmanDecode(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                #print(text)
                res += dictionary[k]
                text = text[len(k):]
                print(res)
    return res

string_4=bitarray()
with open('bacillus_encoded_2.bin','rb') as fh:
	string_4.fromfile(fh)
