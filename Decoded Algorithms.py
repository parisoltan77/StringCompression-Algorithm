# Programmed by Soltanzadeh & Tabatabaee
# String-Compression Decoded Algorithm

import sys
from re import match

#Decoding:
def decompress(inputString):
	outputString = ''
	lastChar = ''
	charIndex = 0
	maxIndex = len(inputString)

	while charIndex < maxIndex:
		nextChar = inputString[charIndex]

		if(match('[A-Z]', nextChar)):
			outputString += nextChar
		else:
			assert(match('[0-9]',nextChar) and charIndex>1 and match('[A-Z]', lastChar) and (lastChar==inputString[charIndex-2]))
			for i in range(int(nextChar)): outputString += lastChar

		charIndex += 1
		lastChar = nextChar

	return outputString

#main
def main():
    input_file = open('Compressed.txt', 'r')
    output_file = open('Decoded.txt', 'w')
    string_text = decompress(input_file.read())
    output_file.write(string_text)
    input_file.close()
    output_file.close()
    return

if __name__ == '__main__':
        main()
