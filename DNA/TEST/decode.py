from bitarray import bitarray
from bitstring import BitStream, BitArray
import numpy as np
def huffmanDecode(dictionary, text):		#huffman decoding function
	res = ""
	i=0
	while text:
		i+=1
		#print(i)
		for k in dictionary:
			if text.startswith(k):
				#print(text)
				res += dictionary[k]
				text = text[len(k):]
				#print(res)
	return res

string=bitarray()
with open('bacillus_encoded_2.bin','rb') as fh:		#opening decoded file
	string.fromfile(fh)
print(len(string))
string_1=BitArray(string).bin					#converting decoded bitarray to string
charlength=int(string_1[:30],2)					#char length
print(charlength)
string_2=int(string_1[30:34],2)					#dicti length
string_3=string_1[34:34+(string_2*23)] 			#dicti string
print(len(string_3))
string_4=string_1[34+(string_2*23):34+(string_2*23)+charlength]		#char string
#string_3=string_1[30+charlength:]
x='abcde'
print(x[-4:5])
print(string_3)
dicti=dict()
#print((len(string_2))/23)
for i in range(0,string_2):
	#print(i)
	x=int(string_3[23*i:23*i+8],2)		#codeword length
	#print(string_3[23*i+16-x:23*i+16])
	#print(type(x))
	#print(string_3[23*i+16:23*i+23])
	dicti[string_3[23*i+16-x:23*i+16]]=chr(int((string_3[23*i+16:23*i+23]),2))
	#print('---')

print(dicti)
#print(huffmanDecode(dicti,string_4))
out=open('bacillus_decoded.fa','w')
out.write(huffmanDecode(dicti,string_4)) 		#calling decode function
#print(string_2)
#charlength=
#string_1=BitArray(string_4[:len(string_2)]).bin
