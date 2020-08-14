from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
import math as mp
import huffman

#tuples = [(38, '\n'), (303, 'N'), (810500, 'G'), (828900, 'C'), (1194405, 'A'), (1208086, 'T')]

x=open('bacillus2.fa')
original_string = x.read()											#reading dna uncommented file  
print(len(original_string))
#string = string_0.replace("\n","")
x.close()


string=bitarray()
with open('bacillus_encoded_2.bin','rb') as fh:		#opening decoded file
	string.fromfile(fh)
print(len(string))
string_1=BitArray(string).bin
print(type(string_1))
charlength=int(string_1[:30],2)						#char length
tuples_length=int(string_1[30:38],2)					#tuples length
print(tuples_length)
string_2=string_1[38:38+(38*(tuples_length))]			#tuples string
string_3=string_1[38+(38*(tuples_length)):charlength]			#encoded string

tuples=[]
for i in range(0,tuples_length):
	tuples.append((int(string_2[38*i:38*i+30],2),chr(int(string_2[38*i+30:38*i+38],2))))
print(tuples)

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

tree = buildTree(tuples)
trim = trimTree(tree)
encoded_string='00000001001011011'
decoded_string=decode(trim,string_3)
print("-------")
print(decoded_string[len(decoded_string)-2])
print("----------")
out=open('bacillus_decoded.fa','w')
out.write(decoded_string)

for i in range(0,len(decoded_string)):
	if decoded_string[i]!=original_string[i]:
		print("error at :",i)
	if i==len(decoded_string)-1:
		print("NO errors")
