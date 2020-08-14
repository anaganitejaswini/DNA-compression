import gzip

x=open('bacillus2.fa')
string = x.read()											#reading dna uncommented file  
print(len(string))
#string = string_0.replace("\n","")
x.close()

string=bytearray(string)
with gzip.open("test.txt.gz", "wb") as f:
	f.write(string)
