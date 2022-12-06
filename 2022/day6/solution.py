import utils.fileReader as fr

signalStream = fr.getTextFileContentAsListOfLines('data/day6.md', trim=True)[0]

found = False
for start in range(0, len(signalStream)): 
    if found:
        break
    for end in range(start, len(signalStream)):
        if end - start == 14 and len(signalStream[start:end]) == len(set(signalStream[start:end])):
            print(end)
            found = True
            break
    # part 1 end - start == 4
