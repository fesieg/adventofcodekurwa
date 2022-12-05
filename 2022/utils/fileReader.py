def getTextFileContentAsListOfLines(filePath, trim):
    with open(filePath) as inputFile:
        inputLines = inputFile.readlines()
    if trim:
        return [x.strip() for x in inputLines]
    else:
        return [x.replace('\n', ' ').replace('\r', '') for x in inputLines]
