import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


FILEPATHLF = './count.xlsx'
dataLF = pd.read_excel(FILEPATHLF)

StrideLFList = pd.DataFrame(dataLF)


First = []
Second = []
First = StrideLFList[['A']]
Second = StrideLFList[['B']]

i = 0
Zero = 0
One = 0
Two = 0
Three = 0

while i < len(StrideLFList):
    print()
    if StrideLFList.iloc[i, 0] - StrideLFList.iloc[i, 1] < 1:
        Zero += 1
    elif StrideLFList.iloc[i, 0] - StrideLFList.iloc[i, 1] < 2:
        One += 1
    elif StrideLFList.iloc[i, 0] - StrideLFList.iloc[i, 1] < 3:
        Two += 1
    else:
        Three += 1
    i += 1

print(Zero, One, Two, Three)
#
# One = 0
# Two = 0
# Three = 0
# Z = 0
# while Z <= 79:
#     if First[Z] - Second[Z] < 2:
#         One += 1
#     elif First[Z] - Second[Z] < 3:
#         Two += 1
#     else:
#         Three += 1
#     Z += 1
#
# print(One, Two, Three)