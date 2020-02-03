import os
import argparse

#First read files
stringToMatch = 'Vertex #,' #all data value lines will contain a (0 and ,) 
lineIndex = 0
startRecord = 0
outputPath = os.getcwd()

#Grab the filename from the argument and place it in fileName
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=argparse.FileType('r'),
                    help="Enter the file name of the SAA hole data(.txt) to be prepared for AutoCAD")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
print(args.filename)
fileName = args.filename.name
if args.verbosity >= 1:
    print("The file to be prepared for AutoCAD is {}".format(args.filename, fileName))
else:
    print(fileName)

#Read out relevant information
# print("Please enter data filepath with extension(Should be txt):", end='')
# fileName = input()
fileNameout = fileName.split(".",1)
print("fileNameout: " + str(fileNameout) + "\nfileNameout[0]: " +fileNameout[0]+ "\nfileNameout[1]: " +fileNameout[1])
print("fileName input received: " + fileName)

print("Path at terminal when executing this file: " + os.getcwd())

# with open(fileName, 'r') as input_file:
# 	print("Input file has been received \n***\n")
# 	contents = input_file.read()
# 	print(contents)
# 	print("\n***\nConcluded reading")
# 	input_file.close()

with open(fileName, 'r') as input_file2, open(outputPath +'/' + fileNameout[0] +'xAutoCADe.txt', 'w') as output_file:
	contentsline = input_file2.readlines()
	for line in contentsline:
		print("Checking..." + line, end='')
		if stringToMatch in line and startRecord == 0:												#Check for 'Vertex #' start of Data
			startRecord = 1																			#Found start of Data variable
			print ("\nFound line: " + line + "\n***Start recording now into output file***\n\n", end='')
		elif startRecord == 1:
			print("Appended line " + str(lineIndex) +" \n")
			truncLine = line.split(" ", 4)																#stop at 4 because everything after isn't used. This probably doesn't save any time but in my head its not worth to split since we don't use the data.
			#print(truncLine)
			for i in range(1, len(truncLine)-1):														#-1 because we only want XYZ from the SAA data
				print("i: " + str(i) + " truncLine: " + truncLine[i] )
				output_file.write(truncLine[i])
			output_file.write("\n")
			lineIndex = lineIndex + 1
	input_file2.close()
	output_file.close()
		
"""*How to use input()*
print("Please enter something: ", end='')
answer = input()
print("Your input was: " + answer)"""