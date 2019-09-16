#declare line length
lineLength = 80

#open file (input)
#open output file ("DAT1.txt")
inFile = open("input.txt", "r")
outFile = open("DAT1.txt", "w")

#declare in margin length
leftMargin = int(input("How many inches for the left margin? "))
rightMargin = int(input("How many inches for the right margin? "))

#get margin integers
leftBuffer = leftMargin * 6 * " "
rightBuffer = rightMargin * 6 * " "

#80 characters in one lineLength
outFile.write("0123456789" * 8 + "\n")

#length left after subtracting margin space from max length
maxLength = lineLength - (leftMargin + rightMargin) * 6

#splits words up and puts into arrays
wordList = inFile.read().split()

#for words in list
#add word to formatted string
#subtract word length from line length
#move runoff words to next line
remLineLength = maxLength
outFile.write(leftBuffer)
for word in wordList:
  if len(word) <= remLineLength - 1:
    outFile.write(word + " ")
    remLineLength -= len(word) + 1
  else:
    extraSpace = remLineLength * " "
    outFile.write(extraSpace + rightBuffer + "\n" + 
                  leftBuffer + word + " ")
    remLineLength = maxLength - len(word) - 1
  
  
#lInch = input("How many inches for the left margin? ")
#rInch = input("How many inches for the right margin? ")
#
#lMargin = int(lInch) * 6
#rMargin = int(rInch) * 6
#my_list = []
#my_list2 = []
#paragraph = lineLength - (lMargin + rMargin)
#
#for i in range(lMargin):
#  my_list.append(" ")
#  
#for i in range(rMargin):
#  my_list2.append(" ")
#
#leftMar = "".join(my_list)
#rightMar = "".join(my_list2) 
#
#fileIn = open("input.txt", "r")
#fileOut = open("dat1.txt", "w")
#splitFile = fileIn.read().split()
#emptySpace = paragraph
#outString = ""
#
#for oneWord in splitFile:
#  if len(oneWord) > paragraph:
#    print("The words exceed the margin size. Please try again")
#  if emptySpace - len(oneWord) < 0:
#    outString = lMargin + fileOut + rMargin + '\n'
#    fileOut.write(outString)
#    outString = ""
#    emptySpace = paragraph
#
#print("012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789")
#print(splitFile)
#
#for line in fileIn:
#  fileOut.write(line)
#  print(line)
  
