from __future__ import annotations
import utils.fileReader as fr

shellLines = fr.getTextFileContentAsListOfLines('data/day7.md', trim=True)[1:]

class AdventTreeScraper:
    def __init__(self) -> None:
        self.totalBelowLimit = 0

    def __call__(self, total):
        self.totalBelowLimit += total

class AdventFile:
    def __init__(self, size: int, name: str) -> None:
        self.size = int(size)
        self.name = name

class AdventDirectory:
    def __init__(self, name: str, parentDir: AdventDirectory) -> None:
        self.directories = []
        self.files = []
        self.name = name
        self.parentDir = parentDir
        self.totalSizeIncludingSubDirs = 0

    def addFile(self, file: AdventFile):
        self.files.append(file)
 
    def walkTreeAndExtractSizes(self, scraper: AdventTreeScraper):
        self.totalSizeIncludingSubDirs = self.getTotalSizeOfSubTree()
        if self.totalSizeIncludingSubDirs <= 100000: scraper(self.totalSizeIncludingSubDirs)
        for d in self.directories:
            d.walkTreeAndExtractSizes(scraper)
    
    def getTotalSizeOfSubTree(self):
        total = sum([f.size for f in self.files])
        for item in self.directories:
            total += item.getTotalSizeOfSubTree()
        return total

    def getDirFromSubDirsByName(self, name):
        for d in self.directories:
            if d.name == name: return d
        return None


# we skip the first line when taking the input
tree = []
rootDir = AdventDirectory('/', None)
tree.append(rootDir)
currentDir = rootDir

for l in range(len(shellLines)):
    line = shellLines[l]
    items = line.split(' ')
    if items[0] == '$':
        if items[1] == "cd":
            if items[2] == '..':
                currentDir = currentDir.parentDir
            elif items[2] == "/": currentDir = rootDir
            else:
                dir = currentDir.getDirFromSubDirsByName(items[2])
                if dir == None:
                    newDir = AdventDirectory(items[2], currentDir)
                    currentDir.directories.append(newDir)
                    currentDir = newDir
                else: currentDir = dir
        elif items[1] == 'ls': pass
    else: 
        if items[0] == 'dir':
            if not items[1] in [c.name for c in currentDir.directories]:
                currentDir.directories.append(AdventDirectory(items[1], currentDir))
        else: currentDir.addFile(AdventFile(items[0], items[1]))


scraper = AdventTreeScraper()
rootDir.walkTreeAndExtractSizes(scraper)
print(scraper.totalBelowLimit)


