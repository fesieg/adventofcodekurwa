def getTextFileContentAsListOfLines(filePath):
    with open(filePath) as inputFile:
        inputLines = inputFile.readlines()
    return [x.strip() for x in inputLines]