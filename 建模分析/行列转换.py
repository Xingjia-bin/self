import pandas as pd
# -*- coding: utf-8 -*-
import xlsxwriter as xw
def xw_toExcel(fileName):  # xlsxwriter库储存数据到excel
    # workbook = xw.Workbook('经纬度.xlsx')
    # # 打开现有的工作表
    # worksheet = workbook.add_worksheet('Sheet1')
    workbook = xw.Workbook(fileName,{'nan_inf_to_errors': True}) # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()
    df1 = pd.read_excel('中值处理.xlsx')# 默认读取工作簿中第一个工作表，默认第一行为表头
    coll=1
    for i in range (1,123,1):
        data = df1.iloc[1, i]  # 读取纬度
        worksheet1.write(0, coll, data)#写入维度值
        coll+=1
        data1 =df1.iloc[0,i+1]
        worksheet1.write(0, coll, data1)
        coll+=1
    workbook.close()
filename='123.xlsx'
xw_toExcel(filename)