import pandas as pd
# -*- coding: utf-8 -*-
import xlsxwriter as xw
def xw_toExcel(fileName):  # xlsxwriter库储存数据到excel
    # workbook = xw.Workbook('经纬度.xlsx')
    #
    # # 打开现有的工作表
    # worksheet = workbook.add_worksheet('Sheet1')
    workbook = xw.Workbook(fileName,{'nan_inf_to_errors': True}) # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()
    df1 = pd.read_excel('IDW.xlsx')# 默认读取工作簿中第一个工作表，默认第一行为表头
    df2 = pd.read_excel('2.xlsx')
    count1=0
    m=1
    n=1
    count2=0
    cow=1
    coll=1
    a=[]
    b=[]
    for i in range (1,14882,121):
        for j in range (count2*100+1,9999,100):
            data1 = df2.iloc[i,1]  # 读取纬度
            data2 = df1.iloc[j,1]
            if  data1 >= data2:
                worksheet1.write(cow, coll, data1) # 写入纬度值

                cow1=2
                for i in range(m, m + 121, 1):
                    data3 = df2.iloc[i - 1, 2]  # 读取重力值
                    worksheet1.write(cow1, coll, data3)  # 写入重力值
                    cow1 = cow1 + 1
                m += 121
                # # a.append(data1)#调试
                coll  +=1#列数佳佳
                count1+=1#计数佳佳
                break
            else:
                worksheet1.write(cow, coll, data2)
                cow2=123
                for u in range(n, n + 100, 1):
                    data3 = df1.iloc[u - 1, 2]  # 读取重力值
                    worksheet1.write(cow2, coll, data3)  # 写入重力值
                    cow2 = cow2 + 1
                n=n+100
                # b.append(data2)
                coll += 1  # 列数佳佳
                print(coll)
                count2+=1
    # m=95*121
    # for i in range (95*121,14882,121):
    #     data1 = df2.iloc[i,1]
    #     worksheet1.write(1, coll,data1 )
    #     cow3=2
    #     for j in range(m, m + 121, 1):
    #         data3 = df2.iloc[m - 1, 2]  # 读取重力值
    #         worksheet1.write(cow3, coll, data3)  # 写入重力值
    #         cow3 = cow3 + 1
    #     m += 121
    #     coll+=1
    # print(len(a))
    # for i in range(len(a)):
    #     worksheet1.write(3, i, a[i])
    print(len(b))
    workbook.close()  # 关闭表


    #
    # for i in range (1,10000,100):
    #     data = df1.iloc[i, 1]  # 读取纬度
    #     coll=coll+1
    #     worksheet1.write(cow, coll, data)#写入维度值
    # # print("读取指定某行某列（单元格）的数据：\n{0}".format(data))
    # coll=1
    # for m in range(1,10000,100):
    #     cow=2
    #     for i in range (m,m+121,1):
    #         data=df.iloc[i-1,2]#读取重力值
    #         worksheet.write(cow,coll,data)#写入重力值
    #         cow=cow+1
    #     coll = coll + 1
    # workbook.close()  # 关闭表
fileName = 'test1.xlsx'

xw_toExcel(fileName)

