from LearnTest import Utils
import pandas as pd

FILEPATH = '.\MVI_9939_15_2_trainDLC_resnet50_SmallFlySecondNov29shuffle1_30000.csv'




# 读取数据
# data = pd.read_excel('.\MVI_9939_15DLC_resnet50_FlySecondNov22shuffle1_20000.xlsx')
# data = pd.read_excel('.\MVI_9939_15_2_trainDLC_resnet50_SmallFlySecondNov29shuffle1_30000.xlsx')
data = pd.read_csv(FILEPATH)


columnsName = ["LFX", "LFY", "LFP",
              "RFX", "RFY", "RFP",
              "LMX", "LMY", "LMP",
              "RMX", "RMY", "RMP",
              "LRX", "LRY", "LRP",
              "RRX", "RRY", "RRP",
              "BX",  "BY",  "BP",
              "MX",  "MY",  "MP"]
df = pd.DataFrame(data)

# print(df)

print("开始删除第一列！")
df.drop(columns='scorer', inplace= True)
df.to_excel("./DFirstOneColumn.xlsx")
print("删除第一列成功！")
# print(df)

print("开始修改列名！")
df.columns = columnsName
df.to_excel("./ChangeColumns.xlsx")
print("最上面一行被改成了列名，修改列名成功！")
# print(df)

print("开始删除前2行！")
df.drop(df.index[0], inplace=True)
df.drop(df.index[0], inplace=True)
print("前2行删除成功！")
df.to_excel("./DFirstTwoIndex.xlsx")
# print(df)

df.reset_index(drop=True, inplace=True)
df.to_excel("./ResetIndex.xlsx")


print("Final Data!!!")
# print(df)

StrideLFList = df.iloc[:, 0:3]
StrideRFList = df.iloc[:, 3:6]
StrideLMList = df.iloc[:, 6:9]
StrideRMList = df.iloc[:, 9:12]
StrideLRList = df.iloc[:, 12:15]
StrideRRList = df.iloc[:, 15:18]
BodyList = df.iloc[:, 18:21]
MouthList = df.iloc[:, 21:24]


# print(StrideLFList.iloc[:, 0:1])
############################################################################################
############################################################################################
############################ 数据处理结束 ######################################################
############################################################################################

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# 分别求出 每一个足部的步距，步频，步速
# 还要求一个总体的步距，步频，步速
SFLF, resultDictLF, resultSumLF = Utils.calculateFunc(StrideLFList)
SFRF, resultDictRF, resultSumRF = Utils.calculateFunc(StrideRFList)
SFLM, resultDictLM, resultSumLM = Utils.calculateFunc(StrideLMList)
SFRM, resultDictRM, resultSumRM = Utils.calculateFunc(StrideRMList)
SFLR, resultDictLR, resultSumLR = Utils.calculateFunc(StrideLRList)
SFRR, resultDictRR, resultSumRR = Utils.calculateFunc(StrideRRList)


print("############################# 步距 ############################")
# 分别打印每一个足部的平均步距
print("左前腿的分时步距是：", resultDictLF)
print("左前腿的平均步距是：", Utils.calculateDictAverageValue(resultDictLF))

print("左前腿的分时步距是：", resultDictRF)
print("右前腿的平均步距是：", Utils.calculateDictAverageValue(resultDictRF))

print("左中腿的分时步距是：", resultDictLM)
print("左中腿的平均步距是：", Utils.calculateDictAverageValue(resultDictLM))

print("右中腿的分时步距是：", resultDictRM)
print("右中腿的平均步距是：", Utils.calculateDictAverageValue(resultDictRM))

print("左后腿的分时步距是：", resultDictLR)
print("左后腿的平均步距是：", Utils.calculateDictAverageValue(resultDictLR))

print("右后腿的分时步距是：", resultDictRR)
print("右后腿的平均步距是：", Utils.calculateDictAverageValue(resultDictRR))


print("############################# 步频 ############################")
print("LF足的分时步频是", Utils.calculateHz(StrideLFList))
print("LF足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideLFList)))

print("RF足的分时步频是", Utils.calculateHz(StrideRFList))
print("RF足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideRFList)))

print("LM足的分时步频是", Utils.calculateHz(StrideLMList))
print("LM足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideLMList)))

print("RM足的分时步频是", Utils.calculateHz(StrideRMList))
print("RM足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideRMList)))

print("LR足的分时步频是", Utils.calculateHz(StrideLRList))
print("LR足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideLRList)))

print("RR足的分时步频是", Utils.calculateHz(StrideRRList))
print("RR足的平均步频是", Utils.calculateDictAverageValue(Utils.calculateHz(StrideRRList)))



################# 问题，不能用腹部的点来判断步距，因为可能存在这种情况，部分足部进行移动，但是身体并没有移动



###### 步速，不能用 步频 * 步速 的方式来计算， 计算爬行速度，就用腹部或者头部的爬行速度来计算
# BodyList = df.iloc[:, 18:21]
# MouthList = df.iloc[:, 21:24]

# 本来是想用头部和腹部两者的平均值，但是后面考虑到，昆虫的头部，可能会存在左右摆动的情况，头部与身体不在一条直线的情况，
# 昆虫的爬行主要是为了身体的移动，所以最终爬行速度将通过腹部的移动速度来计算
SFBody, resultDictBody, resultSumBody = Utils.calculateFunc(BodyList)

# resultSumBody： 记录的是每一次身体部位移动的距离之和，
time = len(BodyList) / 24
# time: 记录的是爬行总的时间
Velocity = resultSumBody / time
print("爬行速度是", Velocity)
