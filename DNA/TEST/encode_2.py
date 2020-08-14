from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import math as mp
from itertools import permutations


with open('bacillus.fa') as fin, open('bacillus2.fa', 'w') as fout:		#creating a file without comments
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

alphabet_1=list(set(string))

'''
perms = [''.join(p) for p in permutations(alphabet_1,k)]

def repetitions(k,perm):
	for i in alphabet_1:
		perm.append(i*k)
	return perm

print(repetitions(k,perms))
print(len(perms))'''

k=1
#for k in range(1,6):
freq = {}
for c in range(0,int(len(string)/k)):
	if string[k*c:k*(c+1)] in freq:
		freq[string[k*c:k*(c+1)]] += 1
	else:
		freq[string[k*c:k*(c+1)]] = 1
#print(freq)
#print(sum(freq.values())) 

total_chars=sum(freq.values())
prob = {k: v/total_chars for k, v in freq.items()}
#print(prob)
#print(sum(prob.values()))

#Entropy
H=0
for i in prob.values():
	if i>0:
		#print(i)
		H-=i*(mp.log(i,2))
		#print(H)
		#print("---")
print(k)
print("Entropy:",H)
print("-----------------------------")


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
dicti={}
#frequency
print(type(freq))
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
	dicti[huffmanCode[char]]=char
	print(' %-4r |%12s' % (char, huffmanCode[char]))


string_encoded=""
for c in range(0,int(len(string)/k)):
	string_encoded+=huffmanCode[string[k*c:k*(c+1)]]
	
print(len(string_encoded))

with open('bacillus_encoded_pair_2.bin','wb') as fh:				#writing final encoded binary file
	bitarray(string_encoded).tofile(fh)
	

	
	
	
