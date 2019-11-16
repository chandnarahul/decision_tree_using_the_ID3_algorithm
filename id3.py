import numpy as np
import pandas as pd
from math import log

eps = np.finfo(float).eps


def calculateEntropy(dictionary: dict, totalNumberOfRecords: int):
    entropySum: int = 0
    for (eItem, eCount) in dictionary.items():
        p = abs(eCount / (totalNumberOfRecords + eps))
        if p == len(dictionary):
            return 0
        entropySum = entropySum - (p * log(p, len(dictionary)))
    return entropySum


dataFrame: pd.DataFrame = pd.read_csv("weather.csv", header=None)
totalRowsInDataSet: int = dataFrame.shape[0]
print('Total number of lines in the file [' + str(totalRowsInDataSet) + ']\n')


def entropyFor(definitionColumn: int, numberOfRecords: int):
    decisionsAndCount: dict = dataFrame[definitionColumn].value_counts()
    localEntropy: float = calculateEntropy(decisionsAndCount, numberOfRecords)
    print('localEntropy ' + str(localEntropy))
    return localEntropy


highestColumnIndex: int = 0


def calculateInformationGain(computeForAttributeIndex: int, decisionColumnIndex: int):
    distinctValuesInAttributeColumn = dataFrame[computeForAttributeIndex].unique()
    decisions = dataFrame[decisionColumnIndex].unique();
    print('decisions =>\n' + str(decisions))
    print(distinctValuesInAttributeColumn)
    informationForEachAttribute: float = 0
    for value in distinctValuesInAttributeColumn:
        filterByDecisionAndColumnValue = dataFrame[
            (dataFrame[computeForAttributeIndex] == value)
            &
            (dataFrame[decisionColumnIndex].isin(decisions))
            ]
        allValuesThatMatchDecisionElement: dict = filterByDecisionAndColumnValue.groupby(
            decisionColumnIndex, as_index=True)[
            decisionColumnIndex].count()
        allValues = len(dataFrame[computeForAttributeIndex][dataFrame[computeForAttributeIndex] == value])
        entropyForEachFeature: float = calculateEntropy(allValuesThatMatchDecisionElement, allValues)
        informationForEachAttribute += (allValues / totalRowsInDataSet) * entropyForEachFeature

    return entropyFor(decisionColumnIndex,) - informationForEachAttribute


def calculateColumnWithHighestEntropy(end: int, decisionColumnIndex: int):
    highestGain: float = eps
    highestIndex: int = 0
    for attributeIndex in range(0, end, 1):
        if attributeIndex == decisionColumnIndex:
            continue

        informationGain: float = calculateInformationGain(attributeIndex, decisionColumnIndex)
        print(informationGain)
        if informationGain > highestGain:
            highestGain = informationGain
            highestIndex = attributeIndex
    return highestIndex


entropyIndex = calculateColumnWithHighestEntropy(len(dataFrame.columns), len(dataFrame.columns) - 1)
