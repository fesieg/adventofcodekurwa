import utils.fileReader as fr

textInput = fr.getTextFileContentAsListOfLines('data/day4.md')

ranges = []
for pair in [x.split(',') for x in textInput]:
    ranges.append([
        [int(pair[0].split('-')[0]),
         int(pair[0].split('-')[1])],
        [int(pair[1].split('-')[0]),
        int(pair[1].split('-')[1])]
        ])

# part1
totalCompleteOverlap = 0
for one, two in ranges:
    if one[0] >= two[0] and one[1] <= two[1] or two[0] >= one[0] and two[1] <= one[1]:
        totalCompleteOverlap += 1

# part2
totalPartialOverlap = 0
for one, two in ranges:
    if not (one[1] < two[0] or one[0] > two[1]):
        totalPartialOverlap += 1

print(totalPartialOverlap)
