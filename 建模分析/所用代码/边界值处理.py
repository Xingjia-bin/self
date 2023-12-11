import pandas as pd
# -*- coding: utf-8 -*-
import xlsxwriter as xw
def xw_toExcel():  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook('he.xlsx',{'nan_inf_to_errors': True})
    #
    # 打开现有的工作表
    worksheet = workbook.add_worksheet('Sheet1')
    worksheet.activate()
    # workbook = xw.Workbook(fileName,{'nan_inf_to_errors': True}) # 创建工作簿
    # worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    # worksheet1.activate()
    df1 = pd.read_excel('he2.xlsx')# 默认读取工作簿中第一个工作表，默认第一行为表头
    df2 = pd.read_excel('2.xlsx')
    count1=0
    m=1
    n=1
    count2=0
    cow=1
    coll=1
    a=[]
    b=[]
    for i in range (0,218,1):
        data1 = df1.iloc[i,193]
        is_null = pd.isnull(data1)
        data2 = df1.iloc[i,194]
        if is_null :
            worksheet.write(i, 1, data2) # 写入纬度值
        else:
            worksheet.write(i, 1, data1)
    workbook.close()

xw_toExcel()