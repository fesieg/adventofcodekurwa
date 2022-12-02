import utils.fileReader as fr

textInput = fr.getTextFileContentAsList('data/day2.md')

rounds = [[textInput[0], textInput[1]] for line in textInput]

print(rounds)
