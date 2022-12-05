import utils.fileReader as fr
from string import ascii_letters

textInput = fr.getTextFileContentAsList('data/day3.md', trim=True)


def part1(textInput):
    total = 0
    for rucksack in [
        [n[:int(len(n) / 2)], 
        n[int(len(n) / 2):]] 
        for n in textInput]:
        total += ascii_letters.index(list(set(rucksack[0]).intersection(rucksack[1]))[0]) + 1
    return total

def part2(textInput):
    rucksacks = [n for n in textInput]
    total = 0
    for i in range(0, len(rucksacks) , 3):
        thisGroup = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
        commonItem = list(set(thisGroup[0]).intersection(thisGroup[1], thisGroup[2]))[0]
        total += ascii_letters.index(commonItem) + 1
    return total

# print(part1(textInput))
print(part2(textInput))