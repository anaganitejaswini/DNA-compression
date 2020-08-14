from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
# Huffman Coding in python

with open('bacillus.fa') as fin, open('bacillus2.fa', 'w') as fout:
	for line in fin:
		if not line.startswith('>'):
			line = line.replace("\n","")
			fout.write(line)
		else:
			fout.write("\n")
            #fout.write(next(fin))
x=open('bacillus2.fa')
string = x.read()
print(len(string))
#string = string_0.replace("\n","")

x.close()

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
dicti={}
for (char, frequency) in freq:
	dicti[huffmanCode[char]]=char
	print(' %-4r |%12s' % (char, huffmanCode[char]))
print(dicti)   


with open('bacillus_encoded.fa', 'w') as fo:
	for char in string:
		fo.write(huffmanCode[char])
#fout = open('bacillus_trial.fa','w')
x=open('bacillus_encoded.fa')
string_2 = x.read()
string_3 = bitarray(string_2)
string_7=""
for char in string:
	string_7+=huffmanCode[char]
print(string_7)
print(string_2)	

with open('bacillus_encoded_2.bin','wb') as fh:
	string_3.tofile(fh)
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
#print(len(string_2))
#print(len(string_4))
#print(BitArray(string_4).bin)
#print(BitArray(string_4[:len(string_2)]).bin)
string_6=BitArray(string_4[:len(string_2)]).bin
print(len(string_6))
string_5='1101001011111110100001110101111000011101111010010'
print(string_5)
out=open('bacillus_decoded.fa','w')
out.write(huffmanDecode(dicti,string_6))
