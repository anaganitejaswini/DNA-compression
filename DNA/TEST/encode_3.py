from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import math as mp
import huffman

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

def frequency (st) :
    freqs = {}
    for ch in st :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs
    
def sortFreq (freqs) :
    letters = freqs.keys()
    tuples = []
    for let in letters :
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples
 

def buildTree(tuples) :
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])                  # get the 2 to combine
        theRest  = tuples[2:]                          # all the others
        combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
        tuples   = theRest + [(combFreq,leastTwo)]     # add branch point to the end
        #print(tuples)
        tuples.sort()                                 # sort it into place
    return tuples[0]            # Return the single tree inside the list

def trimTree (tree) :
     # Trim the freq counters off, leaving just the letters
    p = tree[1]                                    # ignore freq count in [0]
    if type(p) == type("") : return p              # if just a leaf, return it
    else : return (trimTree(p[0]), trimTree(p[1])) # trim left then right and recombine

codes={}
def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat                # A leaf. set its code
    else  :                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1")    # then do the right branch.
        
def encode (st) :
    global codes
    output = ""
    for ch in st : output += codes[ch]
    return output


freqs = frequency(string)   
tuples = sortFreq(freqs)
tree = buildTree(tuples)
trim = trimTree(tree)
print(tuples)
print("------------------------------")
print(freqs)
assignCodes(trim)
encoded_string=encode(string)
print(codes)

print(len(encode(string)))

def decode(tree,st):
	output=""
	p=tree
	for bit in st:
		if bit=="0":
			p=p[0]
		else:
			p=p[1]
		if type(p) == type(""):
			output+=p
			p=tree
	return output

print("---------------")
print(tree[1])
charlength=(bin(len(encoded_string))[2:]).zfill(30)				#length of char string in binary form
decoded_string=decode(trim,encoded_string)
print(len(decoded_string))
for i in range(0,len(decoded_string)):
	if decoded_string[i]!=string[i]:
		print("error at :",i)
string_2=''
string_2+=bin(len(tuples))[2:].zfill(8)
for i in tuples:
	#print(bin(len(tuples))[2:].zfill(8))
	#print(bin(i[0]))
	#print(bin(i[0])[2:])
	string_2+=bin(i[0])[2:].zfill(30)
	#print(bin(i[0])[2:].zfill(30))
	#print("")
	string_2+=bin(ord(i[1]))[2:].zfill(8)
	#print(bin(ord(i[1]))[2:].zfill(8))

encoded_string_2=''.join((charlength,string_2,encoded_string))
with open('bacillus_encoded_2.bin','wb') as fh:				#writing final encoded binary file
	bitarray(encoded_string_2).tofile(fh)

#string_2=
