inFile = open('infile.txt', 'r', encoding='utf8')
outFile = open('outfile.txt', 'w', encoding='utf8')

text = inFile.read()
print(text)

inFile.close()
outFile.close()

