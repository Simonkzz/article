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
FILEPATHLF = './FinalData/sub/LFColumns.xlsx'
dataLF = pd.read_excel(FILEPATHLF)
StrideLFList = pd.DataFrame(dataLF)
StrideLFList[StrideLFList.LFP > 0.8].to_excel("./FinalData/sub/sub/LLLLFFFColumns.xlsx", index=False)
data1 = pd.read_excel("./FinalData/sub/sub/LLLLFFFColumns.xlsx")
StrideLFList = pd.DataFrame(data1)


####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

# 第一条数据的X值
X_Init = StrideLFList.iloc[0, 1]
# 第一条数据的Y值
Y_Init = StrideLFList.iloc[0, 2]

X_Sum = X_Init
Y_Sum = Y_Init

# 步频
StrideFrequency = 0
Count = 1

print(type(StrideLFList))
# i是标记第几条数据，上述初始化的为第0条，此处i初始化为1，将第1条与其比较
i = 1

print("----")

print(len(StrideLFList) - 1)
print(X_Init)
print(Y_Init)
XL = []
YL = []
# 存什么， 记录序号
Number = []
flag = 0
# 首先，过滤的全是大于0.8的，然后如果当前数据与前一条数据大于5，并且如果与后一条数据大于5，则舍弃，如果与当前数据大于5，与后一条数据小于5
# 循环
# 过滤精准度小于0.8的所有词条
# math.fabs: 返回绝对值
# i初始化值为1
while i < (len(StrideLFList) - 2):
    if StrideLFList.iloc[i, 3] >= 0.8:
        if math.fabs(StrideLFList.iloc[i, 1] - X_Init) < 1.5 and math.fabs(StrideLFList.iloc[i, 2] - Y_Init) < 1.5:
            # 如果当前数据与前一条数据的x与y相差的像素值小于1.5，则将其两帧左前足对应的x,y轴坐标值之间的差值看作误差，认为该两帧为同一个落脚点
            X_Sum += StrideLFList.iloc[i, 1]
            Y_Sum += StrideLFList.iloc[i, 2]
            # 求同一个落脚点的X,Y轴的坐标值总和，最后求平均值，用作该落脚点的最后坐标值。
            # 更新对比的值
            X_Init = StrideLFList.iloc[i, 1]
            Y_Init = StrideLFList.iloc[i, 2]
            # 用作求平均值， Count
            Count += 1

            # 如果超过1.5则抛弃掉。
            # 大家可能会问一个问题。如果他是混杂在其中的，比如果像这样，这个是不影响的，因为最终是求平均值的
            # 好的吧前后相差1.5像素值的帧值抛弃掉
            # 如果当前值与前后两个值相差都小于1.5
            # 这个是有用的
        elif math.fabs(StrideLFList.iloc[i, 1] - StrideLFList.iloc[i+1, 1]) < 1.5 and math.fabs(StrideLFList.iloc[i, 2] - StrideLFList.iloc[i+1, 2]) < 1.5:
            # 第二个落脚点的第一帧与上一个落脚点的最后一帧，相差肯定不止1.5个像素，所以上一个if不成立，但是却与第二个落脚点的第二帧相差1.5像素之内

            # 步频 加1
            StrideFrequency += 1

            # 求上一个落脚点的平均值
            X = X_Sum / Count
            Y = Y_Sum / Count
            # 分别把X，Y放对应的数组里面

            # 吧平均值存起来
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

# 本段视频中所有落脚点的数量，以及对应落脚点帧的第一个帧位置序号Number数组
StrideFrequency = len(XL) - 1

#
StrideL = []



## 得到了所有可以确定的x,y轴坐标


def calStride(x1, x2, y1, y2):
    Result = math.sqrt(math.fabs(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)))
    return Result

Stride = []
i = 0
TempM = []
print("111")
print(len(XL))

# 计算所有落脚点之间的距离， A与B，B与C等等，存放在Stride里面
while i < len(XL)-1:
    Temp = calStride(XL[i], XL[i+1], YL[i], YL[i+1])
    # print(XL[i], XL[i+1], YL[i], YL[i+1])
    # print(Temp)
    Stride.append(Temp)
    i += 1

# Number里面存放的是帧的位置， Stride存放的是所有的步距 一个85， 一个84不影响
print(i)
print("00000000000", len(Number), len(Stride))
# for i in Number:
#     print(i)




# Stride第一个为帧数，第二个为计算之后的步幅
YYY = []
i = 0
LastNumber = []
######################################################################################步距在这里#####################
while i < len(Stride)-1:
    # 舍弃大于300， 小于10个像素的步距，作为误差
    if Stride[i] < 300 and Stride[i] > 10:
        #YYY存放的是比较合理的
        YYY.append(Stride[i])
        # LastNumber存放的是合理步距对应的帧的位置编号
        LastNumber.append(Number[i])
    i += 1

############################################
############################# YYY步距，LastNumber用来测步频
############################################
print("LastNumber表示的是最终的帧数", len(LastNumber), len(YYY))

# 这两个数组存储了有用数据
# i = 0
# while i < len(YYY)-1:
#     print(LastNumber[i], YYY[i])
#     i += 1
for i in YYY:
    print(i)




######################################################
#################################### 处理频率 CountNL
#####################################################
CountN = 0
Mid = 0
CountNL = []
FrequencyToNumber = []
# 算的是什么  频率 计算
for i in LastNumber:
    # 计算每100帧的落脚点数量， 比如1-100，101-200帧的落脚点数量等等
    if i > Mid*100 and i < (Mid+1)*100:
        CountN += 1
    else:
        # print("CountNL")
        FrequencyToNumber.append(i)
        CountNL.append(CountN)
        Mid += 1
        CountN = 1

print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(FrequencyToNumber)
print(CountNL)                                                      # CountNL计算的是步频



# for i in CountNL:
#     print(i)

###############################################
#################### 处理速度
###############################################
SpeedList = []
StrideList = []
# LastNumber YYY
i = 0
################################################################################ 计算的是速度
while i < len(LastNumber)-1:
    timeTemp = LastNumber[i+1] - LastNumber[i]  # 合理步距前后落脚点的帧的序号，用来计算时间
    timeTemp = timeTemp / 100
    Long = YYY[i]
    Long = (Long * 4.8) / 238.0                                         # 长度/时间 = 速度
    StrideList.append(Long)                                             # 吧对应像素长度转换为实际长度   步距


    Speed = Long / timeTemp                                                   # 速度

    if (timeTemp > 0.1) and (Long < 3):
        #print(timeTemp, Long)
        # print(Speed)
        SpeedList.append(Speed)
        # print(SpeedList[i], SpeedList[i-1])
    else:
        SpeedList.append(SpeedList[i - 1])

    i += 1


# for i in SpeedList:
#     print("速度是", i)




#########################################################
#########################################################
########################################
#########################################################
#########################################################
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
x1 = LastNumber
x2 = x1[0:60]
print(FrequencyToNumber)
x3 = FrequencyToNumber
y = StrideList
# y像素距离的集合
# y = YYY

plt.title("Left forefoot, relationship between Distance, Speed and Frequency")
plt.xlabel("serial number")
plt.ylabel("value")

plt.plot(x2, y, c='red', marker='o')
plt.plot(x2, SpeedList, c='green', marker='o')
print(x3, CountNL)
plt.plot(x3, CountNL, c='blue', marker='o')


# plt.plot(x1, np.linspace(np.mean(y), np.mean(y), 61), c='blue')
# 相同的数据，不同的位置，也可以放在一个图上
plt.legend(['Step Distance', 'Step Speed', 'Step Frequency'], loc='best')

n = max(LastNumber)
plt.xticks(np.arange(0, n, step=100), fontsize=10)

plt.show()


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

CountNL.sort()
print("速度的区间是", CountNL[0], CountNL[len(CountNL)-1])

SpeedList.sort()
print("速度的区间是", SpeedList[0], SpeedList[len(SpeedList)-1])

StrideList.sort()
print("步幅的区间是", StrideList[0], StrideList[len(StrideList) - 1])
#print("步频的区间是", )

# for i in LastNumber:
#     print(i)
#
# for i in YYY:
#     print(i)
print(len(x1),len(StrideList), len(LastNumber))
