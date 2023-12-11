import pandas as pd
# -*- coding: utf-8 -*-
import xlsxwriter as xw
def xw_toExcel(fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()
    df = pd.read_excel('final.3.xlsx')# 默认读取工作簿中第一个工作表，默认第一行为表头
    cow=1
    coll=1

    for i in range (0,57596,238):
        data = df.iloc[i, 1]  # 读取纬度
        worksheet1.write(cow, coll, data)#写入维度值
        coll = coll + 1
    # print("读取指定某行某列（单元格）的数据：\n{0}".format(data))
    coll=1
    for m in range(0,57596,238):
        cow=2
        for i in range (m,m+238,1):
            data=df.iloc[i,2]#读取结果
            worksheet1.write(cow,coll,data)#写入重力值
            cow=cow+1
        coll = coll + 1
    workbook.close()  # 关闭表
fileName = 'final3.0.xlsx'

xw_toExcel(fileName)

