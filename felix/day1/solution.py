import utils.fileReader as fr

textInput = fr.getTextFileContentAsList('data/day1.md')

elves = []

for line in textInput:
    if textInput.index(line) == 0 or line == '':
        elves.append([])
    elif len(line):
        elves[len(elves) - 1].append(int(line))

elves = [sum(elf) for elf in elves]

highest = max(elves)
elves.pop(elves.index(highest))

secondHighest = max(elves)
elves.pop(elves.index(secondHighest))

thirdHighest = max(elves)

print(highest + secondHighest + thirdHighest)
