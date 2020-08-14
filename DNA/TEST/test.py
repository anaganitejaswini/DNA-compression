from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import json
import binascii
# Huffman Coding in python
'''
with open('trial.fa') as fin, open('bacillus2.fa', 'w') as fout:
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
print(huffmanCode)

with open('bacillus_encoded.fa', 'w') as fo:
	for char in string:
		fo.write(huffmanCode[char])
#fout = open('bacillus_trial.fa','w')
x=open('bacillus_encoded.fa')
string_2 = x.read()
string_3 = bitarray(string_2)
string_7=""
n=int('0b1000001',2)
#print(binascii.unhexlify('%x' '%n'))
print(bin(ord('A')))

#for char in dicti:
	#print(char)
	#string_7+=bin(ord(dicti[char]))
	#string_7+=char
	#string_7+=" "
#s=json.dumps(dicti).encode('utf-8')
s=json.dumps(dicti)
string_7="".join((format(ord(i),'b')).zfill(8) for i in s)
print(len(string_7))
print("-----")
#jsn="".join(chr(int(x,2)) for x in string_7.split())
#variables2=json.loads(jsn)
#print(variables2)
dict_length=(bin(len(string_7)).replace("0b","")).zfill(16)
dict_l_l=(bin(len(dict_length)).replace("0b","")).zfill(8)
#dict_l_l=len(dict_length)
print(dict_length)
print(dict_l_l)
#string_7 = ''.join((dict_length,string_7))
def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary)
    d = json.loads(jsn)  
    return d

dct = binary_to_dict(string_7)
print(dct)
#variables2=json.loads(s.decode('utf-8'))

print(string_7)
print("-----")
string_9=""
for char in string:
	string_9+=huffmanCode[char]
char_length=len(string_9)
print(char_length)
string_7 = ''.join((string_7,string_9))
string_7 = string_7.replace('b', '')
x2=len(string_7)
string_8=bitarray(string_7)	
print(string_7)
print(len(string_7))
#print(string_2)	


with open('bacillus_encoded_2.bin','wb') as fh:
	string_8.tofile(fh)

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
#print(string_4)
#print(BitArray(string_4).bin)
#print(BitArray(string_4[:len(string_2)]).bin)
string_6=BitArray(string_4[:len(string_2)]).bin
#print(len(string_6))
string_5='1101001011111110100001110101111000011101111010010'
#print(string_5)
out=open('bacillus_decoded.fa','w')
#out.write(huffmanDecode(dicti,string_6))
	'''

import string 

selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
def word_count_2(line):

	d = dict.fromkeys(selected_words, 0)
	line = line.strip()  
	line = line.lower()
	line = line.translate(line.maketrans("", "", string.punctuation)) 
	words = line.split(" ")
	for word in words: 
		# Check if the word is already in dictionary 
		if word in selected_words: 
			# Increment count of word by 1 
			d[word] = d[word]+1
	print("------------------------------")
	return d

text2 = "I had a hard time finding a second year calendar, this is the only one I came across and it is great!  Large enough to write in the squares and has a spot to put that month's picture in as well as some memories. The first two years they change so much I like to jot everything down so I can keep track of all the big milestones...and little ones!  I find it is easier to do this on a calendar vs a baby book.  This way you can fill out the baby book later and have a great reference to do so!"
#print( word_count('the quick brown fox fox jumps over the lazy dog awesome great awesome fantastic great love horrible love love horrible .'))
print(word_count_2(text2))

