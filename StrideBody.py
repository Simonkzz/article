import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
FILEPATHLF = './FinalData/sub/BodyColumns.xlsx'
dataLR = pd.read_excel(FILEPATHLF)
StrideLRList = pd.DataFrame(dataLR)
StrideLRList[StrideLRList.BP > 0.8].to_excel("./FinalData/sub/sub/BBBBBBBColumns.xlsx", index=False)
data1 = pd.read_excel("./FinalData/sub/sub/BBBBBBBColumns.xlsx")
StrideLFList = pd.DataFrame(data1)


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

X_Init = StrideLFList.iloc[0, 1]
Y_Init = StrideLFList.iloc[0, 2]
X_Sum = X_Init
Y_Sum = Y_Init

# 步频
StrideFrequency = 0
Count = 1

print(type(StrideLFList))
i = 1

print("----")

print(len(StrideLFList) - 1)
print(X_Init)
print(Y_Init)
XL = []
YL = []
Number = []
flag = 0
# 首先，过滤的全是大于0.8的，然后如果当前数据与前一条数据大于5，并且如果与后一条数据大于5，则舍弃，如果与当前数据大于5，与后一条数据小于5
while i < (len(StrideLFList) - 2):
    if StrideLFList.iloc[i, 3] >= 0.8:
        if math.fabs(StrideLFList.iloc[i, 1] - X_Init) < 1.5 and math.fabs(StrideLFList.iloc[i, 2] - Y_Init) < 1.5:
            X_Sum += StrideLFList.iloc[i, 1]
            Y_Sum += StrideLFList.iloc[i, 2]
            X_Init = StrideLFList.iloc[i, 1]
            Y_Init = StrideLFList.iloc[i, 2]
            Count += 1
        elif math.fabs(StrideLFList.iloc[i, 1] - StrideLFList.iloc[i+1, 1]) < 1.5 and math.fabs(StrideLFList.iloc[i, 2] - StrideLFList.iloc[i+1, 2]) < 1.5:

            # 这个是有用的
            StrideFrequency += 1
            X = X_Sum / Count
            Y = Y_Sum / Count
            # 分别把X，Y放对应的数组里面

            XL.append(X)
            YL.append(Y)
            # 记录序号
            Number.append(i)

            # 重新开始一个点之后，第一个点的坐标需要先初始化
            X_Init = StrideLFList.iloc[i, 1]
            Y_Init = StrideLFList.iloc[i, 2]
            X_Sum = X_Init
            Y_Sum = Y_Init
            Count = 1
    i += 1

StrideFrequency = len(XL) - 1
StrideL = []

print(len(XL))
print(len(YL))

## 得到了所有可以确定的x,y轴坐标


print("============")



# plt.figure(figsize=(5, 3))
# x = np.linspace(1, 85, 85)
# plt.plot(x, XL, c='black', ls='dotted')
# plt.plot(x, YL, c='green', ls='dotted')
# plt.show()

def calStride(x1, x2, y1, y2):
    Result = math.sqrt(math.fabs(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)))
    return Result

Stride = []
i = 0
TempM = []
print("111")
print(len(XL))
while i < len(XL)-1:
    Temp = calStride(XL[i], XL[i+1], YL[i], YL[i+1])
    # print(XL[i], XL[i+1], YL[i], YL[i+1])
    # print(Temp)
    Stride.append(Temp)
    i += 1

print(i)
print("00000000000", len(Number), len(Stride))
# for i in Number:
#     print(i)

# Stride第一个为帧数，第二个为计算之后的步幅
YYY = []
i = 0
LastNumber = []
while i < len(Stride)-1:
    if Stride[i] < 300 and Stride[i] > 10:
        YYY.append(Stride[i])
        LastNumber.append(Number[i])
    i += 1


print("LastNumber表示的是最终的帧数", len(LastNumber), len(YYY))

print("===")
print(len(YYY))
print("===")


# 这两个数组存储了有用数据
i = 0
while i < len(YYY)-1:
    print(LastNumber[i], YYY[i])
    i += 1
for i in YYY:
    print(i)

# 处理频率
CountN = 0
Mid = 0
CountNL = []
FrequencyToNumber = []
for i in LastNumber:
    if i > Mid*100 and i < (Mid+1)*100:
        CountN += 1
    else:
        # print("CountNL")
        FrequencyToNumber.append(i)
        CountNL.append(CountN)
        Mid += 1
        CountN = 1


for i in CountNL:
    print(i)

# 处理速度
SpeedList = []
StrideList = []
# LastNumber YYY
i = 0

print('=====', LastNumber,'=====', StrideList,'=====', YYY)



while i < len(LastNumber)-1:
    timeTemp = LastNumber[i+1] - LastNumber[i]
    timeTemp = timeTemp / 100
    Long = YYY[i]
    Long = (Long * 4.8) / 238.0
    StrideList.append(Long)
    # Long是像素的数量 每个像素0.04cm, 192.5个像素， 4，7cm

    Speed = Long / timeTemp

    print("XXXXMMMM")
    if (Long < 3):
        print(timeTemp, Long)
        # print(Speed)
        SpeedList.append(Speed)
        # print(SpeedList[i], SpeedList[i-1])
    else:
        SpeedList.append(SpeedList[i-1])

    i += 1


print(len(StrideList), len(LastNumber))

for i in SpeedList:
    print("速度是", i)



# 7
# 7
# 11
# 8
# 9
# 11
# 7

##################################
############ 这是按列来的
# print(data.iloc[1, 2]) 按位置取数

# 1、首先遍历StrideLFList,把所有精度低于90的都舍弃掉，
# 同时如果x,y值与前一个相差在3的都记做同一个点，x求和，y求和并且计数，
# 如果遇到相差在3以上的，则求均值，作为上一个点的坐标，与上上一个点求距离，存放在数组中，频率+1


# 5.8  6.1mm
# 7.7cm 一个像素0.04cm 7.7/0.04=192.5个像素  6.1/192.5 *551.83= 17.71589mm

# 7.400438861565283    0.23449
# 93.62454742275118    2.966



# plt.figure(figsize=(5, 3))

plt.rcParams['figure.figsize']=(12.8, 7.2)

# X轴应该是帧数值
x1 = LastNumber  # 62
x2 = x1[0:144]
x3 = FrequencyToNumber
y = StrideList # 57
# y = YYY

plt.title("Right hindfoot, relationship between Distance, Speed and Frequency")
plt.xlabel("serial number")
plt.ylabel("value")

plt.plot(x2, y, c='red', marker='o')
plt.plot(x2, SpeedList, c='green', marker='o')
plt.plot(x3, CountNL, c='blue', marker='o')
# plt.plot(x1, np.linspace(np.mean(y), np.mean(y), 62), c='blue')

# 相同的数据，不同的位置，也可以放在一个图上

plt.legend(['Step Distance', 'Step Speed', 'Step Frequency'], loc='best')

plt.yticks(fontsize=10)

n = max(LastNumber)

plt.xticks(np.arange(0, n, step=100), fontsize=10)
plt.show()


print("区间")
YYY.sort()
print(YYY[0])
print(YYY[len(YYY)-1])
print("区间")
print(4.5*YYY[0] / 192.5)
print(4.5*YYY[len(YYY)-1] / 192.5)
print("======")
print(calStride(244, 336, 723, 610))
print(calStride(556, 544, 836, 938))


# 不加条件  129条数据 区间5.44-1499
# 0-500    123条数据
# 0-300    122条数据
# 0-200    117条数据


############################
# 最终数据，速度存放放在SpeedList中，
# 步幅存放在 YYY中
# 频率根据LastNumber进行计算
print("速度的长度是", len(SpeedList))
print("步幅的长度是", len(YYY))
print("步频的长度是,记录的是帧数，根据帧数，每100帧一秒，计算频率", len(LastNumber))
SpeedList.sort()

print("速度的区间是", SpeedList[0], SpeedList[len(SpeedList)-1])
print("步幅的区间是", )
#print("步频的区间是", )

# for i in LastNumber:
#     print(i)

for i in YYY:
    print(i)

