import pandas as pd
import math

FILEPATH = 'FinalData/4FinalResetIndex.xlsx'
data = pd.read_excel(FILEPATH)
df = pd.DataFrame(data)

print(df)

###############################
############### 注意，这里是左包含，右不包含，但是因为每一组只有前面两列数据是所必要的
###############################
StrideLFList = df.iloc[:, 0:3]
StrideRFList = df.iloc[:, 3:6]
StrideLMList = df.iloc[:, 6:9]
StrideRMList = df.iloc[:, 9:12]
StrideLRList = df.iloc[:, 12:15]
StrideRRList = df.iloc[:, 15:18]
BodyList = df.iloc[:, 18:21]

for i in StrideLFList:
    print(i)

print(type(len(StrideLFList)))
print(StrideLFList)
print("============")
print(StrideLFList.iloc[0][0])
print(type(float(StrideLFList.iloc[0][0])))



StrideFrequency = 0
i = 0
InitValue = StrideLFList.iloc[i]

print(type((InitValue[0])))
print(type(StrideLFList.iloc[i+1][0]))
print("测试类型")
resultDict = {}
resultSum = 0


##################################
############ 这是按列来的
# print(data.iloc[1, 2]) 按位置取数

# 1、首先遍历StrideLFList,把所有精度低于90的都舍弃掉，
# 同时如果x,y值与前一个相差在3的都记做同一个点，x求和，y求和并且计数，
# 如果遇到相差在3以上的，则求均值，作为上一个点的坐标，与上上一个点求距离，存放在数组中，频率+1



# 计算一下步距（也就是步幅）和步频，传入的参数就是足部的信息，
# 比如说我现在要计算左前足的信息，吧左前足的数据传进去就可以了
def culculateFunc(StrideList):
    StrideFrequency = 0
    i = 0
    # .iloc是什么意思
    InitValue = StrideList.iloc[i]

    print(type((InitValue[0])))
    print(type(StrideList.iloc[i + 1][0]))
    print("测试类型")
    resultSum = 0
    while i < (len(StrideList) - 1):
        result = math.fabs(math.sqrt(math.fabs(pow((float(InitValue[0])-float(StrideLFList.iloc[i+1][0])), 2) - pow((float(InitValue[1])-float(StrideLFList.iloc[i+1][1])), 2))))
        print(i)
        print("本次移动距离为：")
        print(result)
        if result >= 3:
            resultDict[i] = result
            resultSum += result
            print(i)
            print(InitValue[0])
            print(InitValue[1])
            StrideFrequency += 1
            InitValue = StrideList.iloc[i+1]
            print("")
        i = i+1

    return StrideFrequency, resultDict, resultSum

SF, rd, rs = culculateFunc(StrideRFList)

print("========")
print(rd[1])
print("========")
print(SF, rd, rs)


#### 有了字典，首先可以求 各个足部的步距
#### 然后求
def culculateHz(StrideList):
    StrideF, resultDict, ResultS = culculateFunc(StrideList)
    hz = 0
    for i in resultDict.keys():
        if i <= 24:
            hz += 1
            print("dayin", i)
    print("苍蝇每秒钟的步频为", hz)
    return hz


# 速度=步距*步频
# 或者用腹部点的移动速度来代表整个虫子的爬行速度
def culculateVelocityByHz(StrideList, resultDict):
    return culculateFunc(StrideList) * culculateHz(resultDict)


def culculateVelocityByBody(StrideList):
    # 根据每秒钟的速度，再求平均值
    culculateFunc(StrideList)
    # 然后继续求24帧的腹部点的移动距离
    return resultDict;








print("HZZZZZZZZZZZZZZZZ")

culculateHz(resultDict)

# while i < (len(StrideLFList) - 1):
#     result = math.fabs(math.sqrt(math.fabs(pow((float(InitValue[0])-float(StrideLFList.iloc[i+1][0])), 2) - pow((float(InitValue[1])-float(StrideLFList.iloc[i+1][1])), 2))))
#     print(i)
#     print("本次移动距离为：")
#     print(result)
#     if result >= 3:
#         resultDict[i] = result
#         resultSum += result
#         print(i)
#         print(InitValue[0])
#         print(InitValue[1])
#         StrideFrequency += 1
#         InitValue = StrideLFList.iloc[i+1]
#         print("")
#     i = i+1



# print(StrideFrequency)
# print("========================================")
# print(resultDict)
# print(len(resultDict))
# print("Average Stride length:")
# print(resultSum/len(resultDict))




##########################################
############### 按行来计算步频，需要计算出帧到帧之间有多少足部进行移动了，比较复杂
############### 可以把这个方法写清楚，写完，与另外一个办法进行比较、、

## 需要用字典对移动的距离进行存储。如果需要计算步频，则以时间为节点（一秒，24帧，或者其他单位时间），从字典中取数据，24对应字典位置，之前的所有值的个数。
## 存在问题，可能字典里面并没有key值为24的值

## 按照这个步骤，分别从不同的List取值，求6个值的和，也就是1秒时间内，南亚苍蝇六个足部移动次数之和，也就记为其步频。




## 速度怎么求
## 同样，求速度的时候，也需要从字典中取值，单位时间1s,则从字典中取24对应值及其之前的值，然后求和，则为单位时间改足部的速度。
## 但是存在问题。苍蝇爬行时，存在角动量的问题。
## 如何解决，
## 1、硬件上，拍摄的时候，使用条形容器进行数据拍摄
## 2、取腹部和头部为爬行方向，任何一个足部的前近距离在爬行方向上进行映射
## 3、干脆，取头部或者腹部的移动数据量进行求速度作为苍蝇的爬行速度。因为苍蝇六条腿不管是从什么方向上进行移动，最终的运动结果就是苍蝇的身体向前移动。从另一个方向上看，腹部的运动量就是各个足部在真正运动方向进行投影之后的结果







# 查看字典的数量
# print("Length:", len(emptyDict))


def speak(self):
    print("my name" + self.Name)

















# print(StrideLFList[2:, 0:1])
#


# print(StrideLFList)
#依次对每个集合进行处理、
#首先是StrideLFList
# for lie in StrideLFList.loc[3:]: #默认打印index标题
#         print(lie)
# b = BV(1, 2)

# print(StrideLFList.loc[[6,7]])
# print(StrideLFList.loc[[6,7]])

# i=0
# # 默认步频为0
# StrideFrequency = 0
# InitValue1 = StrideLFList.iloc[:, 0:1]
# print("Init Value是")
# print(type(InitValue1)) # <class 'pandas.core.frame.DataFrame'>
# print(InitValue1)

# print(pd.to_numeric(StrideLFList.iloc[:, 0:1]))
# print(type(StrideLFList["LFX"]))
# print(StrideLFList["DL"])
###########################################
#############这个方法是可行的，但是存在字符串
# print("xxxxx")
# StrideLFList[['LFX']] = StrideLFList[['LFX']].astype("float")
# print(type(StrideLFList[['LFX']]))


# InitValue = InitValue1.to_dict()
# print(type(InitValue)) # <class 'dict'>
# print(InitValue["DL"]) # {'DL': {2: 684.9628296}, 'DC': {2: 427.686554}, 'DLC_resnet50_FlySecondNov22shuffle1_20000': {2: 0.279593527}}
#

# while i < len(StrideLFList):
#     if math.fabs(InitValue - StrideLFList[i]) >= 3:
#         StrideFrequency += 1
#         InitValue = StrideLFList[i]
#     i = i+1
#
# print("111")


# print(df.iloc[:, 0:1].loc[[0,1,2,3,4,5]])
# print(df.iloc[:, 0:1].loc[0:5])
# print(df[["DL", "DC"]].iloc[2:])
# print("=======")


