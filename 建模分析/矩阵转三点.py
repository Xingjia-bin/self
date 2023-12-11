import pandas as pd
# -*- coding: utf-8 -*-
import xlsxwriter as xw
def xw_toExcel(fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()
    df = pd.read_excel('待转.xlsx')# 默认读取工作簿中第一个工作表，默认第一行为表头
    cow=1
    coll=0
    for j in range(1, 121, 1):
        for i in range (1,120,1):
            data1 = df.iloc[i, 0]  # 读取经度
            data2 =df.iloc[i,j] #数据值
            data3 =df.iloc[0,j]
            worksheet1.write(cow, 0, data1)#写入经度值
            worksheet1.write(cow, 1, data3)#写入维度值
            worksheet1.write(cow, 2, data2)#写入数据值
            cow+=1
    # print("读取指定某行某列（单元格）的数据：\n{0}".format(data))
    # coll=1
    # for m in range(1,14883,121):
    #     cow=2
    #     for i in range (m,m+121,1):
    #         data=df.iloc[i-1,2]#读取重力值
    #         worksheet1.write(cow,coll,data)#写入重力值
    #         cow=cow+1
    #     coll = coll + 1
    workbook.close()  # 关闭表
fileName = 'final.xlsx'

xw_toExcel(fileName)

