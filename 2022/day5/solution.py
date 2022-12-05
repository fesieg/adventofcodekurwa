import utils.fileReader as fr
import re

textInput = fr.getTextFileContentAsListOfLines('data/day5.md', trim=False)

class CraneStack:
    def __init__(self, items) -> None:
        self.items = items

    def returnAndRemoveMultipleFromTop(self, x):
        returnStack = self.items[:x] 
        self.items = self.items[x:len(self.items)]
        return returnStack

    def returnAndRemoveTopItem(self):
        removedItem = self.items[0]
        self.items = self.items[1:]
        return removedItem

    def addListOfItemsToStack(self, items):
        if len(items) == 1:
            self.addItemToStack(items[0])
        else:
            for n in range(len(items) - 1, - 1 , - 1):
                self.addItemToStack(items[n])


    def addItemToStack(self, item):
        self.items.insert(0, item)


class CraneMap:
    def __init__(self, map):
        craneMap = [line for line in map if '[' in line]
        planMap = [line for line in map if 'move' in line]
        # initialize crane stacks and items

        numOfStacks = self.getNumberOfStacksInMap(planMap)
        # why make it easy when you can make it difficult
        indexMap = {}
        # the mapped index of the stack is mappable to the index of the char in the line like below
        # this way we don't have to trim and cut the input 
        for n in range(0, numOfStacks + 1):
            indexMap[n * 4 + 1] = n
        
        stacks = [[] for _ in range(numOfStacks)]

        for line in craneMap:
            for c in range(len(line)):
                if line[c].isalpha():
                    stacks[indexMap[c]] += line[c]
        
        self.craneStacks = [CraneStack(stack) for stack in stacks] 
        
        self.operations = []
        # initialize operation plan via regex
        for n in [re.findall(r'\b\d+\b', line) for line in planMap]:
            self.operations.append([int(x) for x in n])


    def runPlanPart1(self):
        for operation in self.operations:
            self.moveItemToNewStackXTimes(x=operation[0], start=operation[1], target=operation[2])


    def runPlanPart2(self):
        for operation in self.operations:
            self.moveXItemsToNewStackAtOnce(x=operation[0], start=operation[1], target=operation[2])


    def getNumberOfStacksInMap(self, map):
        # find highest number items are moved to
        # this isn't really a solution as no items might ever be moved to the highest numbered index
        # but it works for all inputs i've tested
        return max([int(l.split('to')[1]) for l in map if 'to' in l])


    def moveXItemsToNewStackAtOnce(self, x, start, target):
        self.craneStacks[target - 1].addListOfItemsToStack(self.craneStacks[start - 1].returnAndRemoveMultipleFromTop(x))
        

    def moveItemToNewStackXTimes(self, x, start, target):
        for n in range(x):
            itemToMove = self.craneStacks[start - 1].returnAndRemoveTopItem()
            self.craneStacks[target - 1].addItemToStack(itemToMove)


craneMap = CraneMap(textInput)
# craneMap.runPlanPart1()
craneMap.runPlanPart2()
print(''.join([c.items[0] for c in craneMap.craneStacks]))