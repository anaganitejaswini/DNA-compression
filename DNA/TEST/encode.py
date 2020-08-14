from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import math as mp

with open('clostridium.fa') as fin, open('bacillus2.fa', 'w') as fout:		#creating a file without comments
	for line in fin:
		if not line.startswith('>'):
			line = line.replace("\n","")
			fout.write(line)
		else:
			fout.write("\n")
            #fout.write(next(fin))
x=open('bacillus2.fa')
string = x.read()											#reading dna uncommented file  
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
        
total_chars=sum(freq.values())
prob = {k: v/total_chars for k, v in freq.items()}
print(prob)
print(sum(prob.values()))

#Entropy 
H=0
for i in prob.values():
	if i>0:
		print(i)
		H-=i*(mp.log(i,2))
		print(H)
		print("---")
print("Entopy:",H)
		

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
print("node:",nodes[0][0])
dicti={}
#frequency
print(type(freq))
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
	dicti[huffmanCode[char]]=char
	print(' %-4r |%12s' % (char, huffmanCode[char]))
string_7=""
for char in dicti:											#creating dictionary string with codeword lengths
	string_7+= bin(len(char))[2:].zfill(8)
	string_7+= char.zfill(8)
	string_7+= bin(ord(dicti[char]))[2:].zfill(7)
	
print(len(string_7))
print(string_7)	
print(dicti)
string_8=""
for char in string:											#creating actual encoded char string
	string_8+= huffmanCode[char]
print("length:",len(string_8))
charlength=(bin(len(string_8))[2:]).zfill(30)				#length of char string in binary form
string_9 =''.join((charlength,((bin(len(dicti)))[2:]).zfill(4),string_7,string_8))
with open('bacillus_encoded_2.bin','wb') as fh:				#writing final encoded binary file
	bitarray(string_9).tofile(fh)
print(len(string_9))
