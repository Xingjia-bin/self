import numpy as np
import pandas as pd

array5 = np.random.randint(1, 100, 10)
array6 = np.random.normal(50, 10, 20)
array12 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
array13 = np.random.rand(3, 4)
array14 = np.random.randint(1, 100, (3, 4))
array16 = np.arange(1, 25).reshape((2, 3, 4))
array19 = np.arange(1, 100, 2)
array20 = np.random.rand(3, 4)
# print(array19.dtype, array20.dtype)
# print(array19.ndim, array20.ndim)
array21 = np.arange(1, 100, 2, dtype=np.int8)
# print(array19.itemsize, array20.itemsize, array21.itemsize)
# print(array19.nbytes, array20.nbytes, array21.nbytes)

# print(isinstance(array20.flat, np.ndarray), isinstance(array20.flat, Iterable))
array22 = array19[:]
# print(array22.base is array19, array22.base is array21)
array23 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(array23[0], array23[array23.size - 1])
# print(array23[-array23.size], array23[-1])
array24 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array24[2])
# print(array24[0][0], array24[-1][-1])
# print(array24[1][1], array24[1, 1])
# array24[1][1] = 10
# print(array24)
# array24[1] = [10, 11, 12]
# print(array24)
# guido_image = plt.imread(r'C:\Users\MCXJB666\Desktop\python\selenium\bd.png')
# print(guido_image)
# data参数表示数据，index参数表示数据的索引（标签）
# 如果没有指定index属性，默认使用数字索引
ser1 = pd.Series(data=[320, 180, 300, 405], index=['一季度', '二季度', '三季度', '四季度'])
# print(ser1)
# 字典中的键就是数据的索引（标签），字典中的值就是数据
ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
# print(ser2)
# print(ser2['一季度'], ser2['三季度'])
# ser2['一季度'] = 380
# print(ser2)
# ser2[1:3] = 400, 500
# print(ser2[ser2>=300])
# print(ser2.describe())

# ser5 = pd.Series(range(5))
# # print(ser5.where(ser5 > 0))
# print(ser5.where(ser5> 1,10))
# import pymysql
#
# # 创建一个MySQL数据库的连接对象
# conn = pymysql.connect(
#     host='localhost', port=3306,
#     user='cat', password='123456',
#     database='school', charset='utf8mb4'
# )
# # 通过SQL从数据库读取数据创建DataFrame
# df5 = pd.read_sql('select * from event', conn, index_col='eno')
# print(df5)
a=list((1,2,3,4))
for i in a:
    print(i)
