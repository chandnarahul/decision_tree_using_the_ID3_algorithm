from math import log

import pandas as pd

dataFrame = pd.read_csv("car.csv", header=None)

totalRowsInDataSet = dataFrame.shape[0]
print('Total number of lines in the file [' + str(totalRowsInDataSet) + ']\n')

lastColumnInDataSet = len(dataFrame.columns) - 1

decisionsAndCount = dataFrame[lastColumnInDataSet].value_counts()

entropy = 0
numberOfDecisions = len(decisionsAndCount);
for decisionCount in range(numberOfDecisions):
    p = decisionsAndCount[decisionCount] / totalRowsInDataSet
    entropy = entropy - (p * log(p, numberOfDecisions))

print('Entropy for decisions is [' + str(entropy) + ']\n')
