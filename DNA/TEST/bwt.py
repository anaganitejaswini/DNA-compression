import argparse
from operator import itemgetter
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
string = x.read()
#string=bw_transform(string)[1]										#reading dna uncommented file  
print(len(string))
#string = string_0.replace("\n","")
x.close()


#BWT
bwt_string=""
#a = input("Enter a string:")
a=string
words = list(a)
list = []
for i in range(len(words)):
    word = a[-1] + a[:-1]
    new = ''.join(word)
    a = new
    list.append(new)
    i += 1
#print(list)
sort = sorted(list)
#print(sort)
for i in range(len(words)):
    element = sort[i]
    last = element[- 1]
    i = i + 1
    bwt_string=bwt_string.join(last)
    
print(bwt_string)
    
def bw_transform(s):
    n = len(s)
    m = sorted([s[i:n]+s[0:i] for i in range(n)])
    I = m.index(s)
    L = ''.join([q[-1] for q in m])
    return (I, L)

def bw_restore(I, L):
    n = len(L)
    X = sorted([(i, x) for i, x in enumerate(L)], key=itemgetter(1))
    print("X----------")
    print(X)

    T = [None for i in range(n)]
    for i, y in enumerate(X):
        j, _ = y
        
        T[j] = i
    print("T: ",T)
    Tx = [I]
    for i in range(1, n):
        Tx.append(T[Tx[i-1]])
    print("Tx:",Tx)

    S = [L[i] for i in Tx]
    S.reverse()
    return ''.join(S)


'''trans_string=bw_transform("banana$")
print(trans_string)
ibwt=bw_restore(trans_string[0],trans_string[1])
print(ibwt)'''




