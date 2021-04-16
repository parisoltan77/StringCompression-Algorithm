# Programmed by Soltanzadeh & Tabatabaee
# String-Compression Encoded Algorithm

import sys
from re import match

#Encoding:
def compress(inputString):
	outputString = ''
	lastChar = ''
	charIndex = 0
	maxIndex = len(inputString)

	while charIndex < maxIndex:

		nextChar = inputString[charIndex]
		assert(match('[A-Z]', nextChar))
		outputString += nextChar
		charIndex += 1

		if(nextChar == lastChar): # fastforward charIndex through the duplicated characters
			count = 0 # counts duplicate characters compressed
			while((charIndex+count<maxIndex) and (inputString[charIndex+count]==lastChar) and (count<9)):
				count += 1
			charIndex += count
			nextChar = str(count)
			outputString += nextChar
		lastChar = nextChar

	return outputString

#main
def main():
    input_file = open('input.txt', 'r')
    output_file = open('Compressed.txt', 'w')
    string_text = compress(input_file.read())
    output_file.write(string_text)
    input_file.close()
    output_file.close()
    return

if __name__ == '__main__':
        main()
