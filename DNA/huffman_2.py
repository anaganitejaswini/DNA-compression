# Huffman Coding in python

with open('bacillus.fa') as fin, open('bacillus2.fa', 'w') as fout:
    for line in fin:
        if not line.startswith('>'):
            fout.write(line)
            #fout.write(next(fin))

x=open('bacillus2.fa')
string_0 = x.read()
string = string_0.replace("\n","")

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
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))


fout=open('bacillus_encoded.txt', 'w')
for char in string:
	fout.write(huffmanCode[char])
'''
with open('bacillus2.fa') as fin, open('bacillus_trial.fa', 'w') as fout:
	for char in fin:
		if char=='\n':
			#fout.write('\n')
		else:
			fout.write(huffmanCode[char])	'''		
		
x=open('bacillus_encoded.txt')
string_2 = x.read()

print(string_2)
