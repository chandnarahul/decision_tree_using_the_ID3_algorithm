from math import log2
inputFile = open("car.csv", "r")

decisionsAndTheirCountMap = {}
labelsAndTheirCountMap = {}
totalNumberOfRowsInFile = 0

for line in inputFile.readlines():
    totalNumberOfRowsInFile = totalNumberOfRowsInFile + 1
    dataAsArray = line.strip().split(',')
    
    lengthOfColumns = len(dataAsArray)
    
    descisionColumnValue = dataAsArray[lengthOfColumns-1]
    
    if descisionColumnValue in decisionsAndTheirCountMap:
        decisionsAndTheirCountMap[descisionColumnValue] = decisionsAndTheirCountMap.get(descisionColumnValue) + 1
    else:
        decisionsAndTheirCountMap[descisionColumnValue] = 1
    
    labelColumnsExcludingDescisionColumn = len(dataAsArray) - 1
    for labelIndex in range(labelColumnsExcludingDescisionColumn):
        labelColumnValue = dataAsArray[labelIndex]
        try:
            labelsAndTheirCountMap[labelIndex].add(labelColumnValue)
        except KeyError:
            labelsAndTheirCountMap[labelIndex] = {labelColumnValue}
      

print ('Total number of lines in the file ['+str(totalNumberOfRowsInFile)+']\n')

print ('Descisions and their count: \n' + str(decisionsAndTheirCountMap) + '\n')

print ('Labels and their count: \n'+str(labelsAndTheirCountMap)+'\n')

entropy = 0
for (descision,count) in decisionsAndTheirCountMap.items():
    p = (count/totalNumberOfRowsInFile)
    entropy = entropy - p * log2(p)

print('Entropy for descisions is ['+str(entropy)+']\n')

for (descision,count) in decisionsAndTheirCountMap.items():
    p = (count/totalNumberOfRowsInFile)
    entropy = entropy - p * log2(p)