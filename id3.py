from math import log
from typing import Dict

inputFile = open("car.csv", "r")

columnsAndTheirCountMap: Dict[int, Dict[str, int]] = {}
totalNumberOfRowsInFile = 0
lengthOfColumns = 0
for line in inputFile.readlines():
    totalNumberOfRowsInFile = totalNumberOfRowsInFile + 1
    dataAsArray = line.strip().split(',')

    lengthOfColumns = len(dataAsArray)

    for labelIndex in range(lengthOfColumns):
        labelColumnValue = dataAsArray[labelIndex]
        if labelIndex in columnsAndTheirCountMap:
            innerDictionary: Dict[str, int] = columnsAndTheirCountMap[labelIndex]
            try:
                innerDictionary[labelColumnValue] = innerDictionary[labelColumnValue] + 1
            except KeyError:
                innerDictionary[labelColumnValue] = 1

            columnsAndTheirCountMap[labelIndex] = innerDictionary
        else:
            innerDictionary: Dict[str, int] = {labelColumnValue: 1}
            columnsAndTheirCountMap[labelIndex] = innerDictionary

print('All columns and their label types: \n' + str(columnsAndTheirCountMap) + '\n')

decisionsAndTheirCountMap = columnsAndTheirCountMap[lengthOfColumns - 1]
print('Total number of lines in the file [' + str(totalNumberOfRowsInFile) + ']\n')

print('Decisions and their count: \n' + str(decisionsAndTheirCountMap) + '\n')

entropy = 0
for (decision, count) in decisionsAndTheirCountMap.items():
    p = (count / totalNumberOfRowsInFile)
    entropy = entropy - (p * log(p, len(decisionsAndTheirCountMap)))

print('Entropy for decisions is [' + str(entropy) + ']\n')
