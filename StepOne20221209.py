import pandas as pd

# 读取数据
# data = pd.read_excel('.\MVI_9939_15DLC_resnet50_FlySecondNov22shuffle1_20000.xlsx')
# data = pd.read_excel('.\MVI_9939_15_2_trainDLC_resnet50_SmallFlySecondNov29shuffle1_30000.xlsx')
data = pd.read_csv('./C0130DLC_effnet_b0_formalBugFiveMay9shuffle1_30000.csv')



# 把对应的列名做修改
columnsName = ["scorer",
              "LFX", "LFY", "LFP",
              "RFX", "RFY", "RFP",
              "LMX", "LMY", "LMP",
              "RMX", "RMY", "RMP",
              "LRX", "LRY", "LRP",
              "RRX", "RRY", "RRP",
              "BX",  "BY",  "BP"]
df = pd.DataFrame(data)

print(df)



print("开始修改列名！")
df.columns = columnsName
df.to_excel("./FinalData/1ChangeColumns.xlsx")
print("最上面一行被改成了列名，修改列名成功！")
print(df)

print("开始删除前2行！")
df.drop(df.index[0], inplace=True)
df.drop(df.index[0], inplace=True)
print("前2行删除成功！")
df.to_excel("./FinalData/2DFirstTwoIndex.xlsx")
print(df)

print("开始删除第一列！")
df.drop(columns='scorer', inplace= True)
df.to_excel("./FinalData/3DFirstOneColumn.xlsx")
print("删除第一列成功！")
print(df)

df.reset_index(drop=True, inplace=True)
df.to_excel("./FinalData/4FinalResetIndex.xlsx")



print("Final Data!!!")
print(df)


# 先分别计算六个足部，每一个足部的步幅。StrideLF, StrideRF, StrideLM, StrideRM,
# StrideLR, StrideRR,分别代表左前足的步幅，右前足的步幅，左中足的步幅，右中足的步幅，
# 左后足的步幅，右后足的步幅。
# 那么首先就要分别取出表格中除第一列（索引列）外，每三个列一组分别用StrideLFList,
# StrideRFList, StrideLMList, StrideRMList, StrideLRList, StrideRRList
# 分别求出，每 一个足部在视频中的足部移动频率




FILEPATH = 'FinalData/4FinalResetIndex.xlsx'
data = pd.read_excel(FILEPATH)
df = pd.DataFrame(data)

print(df)

###############################
############### 注意，这里是左包含，右不包含，但是因为每一组只有前面两列数据是所必要的
###############################
StrideLFList = df.iloc[:, 1:4]
StrideLFList.to_excel("./FinalData/sub/LFColumns.xlsx")
StrideRFList = df.iloc[:, 4:7]
StrideRFList.to_excel("./FinalData/sub/RFColumns.xlsx")
StrideLMList = df.iloc[:, 7:10]
StrideLMList.to_excel("./FinalData/sub/LMColumns.xlsx")
StrideRMList = df.iloc[:, 10:13]
StrideRMList.to_excel("./FinalData/sub/RMColumns.xlsx")
StrideLRList = df.iloc[:, 13:16]
StrideLRList.to_excel("./FinalData/sub/LRColumns.xlsx")
StrideRRList = df.iloc[:, 16:19]
StrideRRList.to_excel("./FinalData/sub/RRColumns.xlsx")
BodyList = df.iloc[:, 19:22]
BodyList.to_excel("./FinalData/sub/BodyColumns.xlsx")

print("操作完成！！！")
