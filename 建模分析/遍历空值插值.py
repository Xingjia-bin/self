import math
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
df=pd.read_excel("2.xlsx")
know_lon=df.iloc[2:11485,0]
know_lon=know_lon.tolist()
know_lat = df.iloc[2:11485,1]
know_lat=know_lat.tolist()
know_z=df.iloc[2:11485,2]
know_z=know_z.tolist()

#更换求距离的函数
def haversine(lon1, lat1, lon2, lat2):
    R =  6372.8
    dLon = radians(lon2 - lon1)
    dLat = radians(lat2 - lat1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    d = R * c
    return d

def IDW(x, y, z, xi, yi):
    lstxyzi = []

    # for p in range(len(xi)):
    lstdist = []
    for s in range(len(x)):
        d = (haversine(x[s], y[s], xi, yi))
        lstdist.append(d)
    lstdist = [1 if x == 0 else x for x in lstdist]
    sumsup = list((1 / np.power(lstdist, 2)))#权重
    suminf = np.sum(sumsup)#权重的和
    z = np.array(z)
    if np.isfinite(sumsup).any() and np.isfinite(suminf):
        sumsup = np.array(sumsup)
        sumsup = np.sum(sumsup * z)
        u = sumsup / suminf
    else:
        u = np.nan
    xyzi = u
    lstxyzi.append(xyzi)
    return u

df1 = pd.read_excel('sum.xlsx')
import numpy as np

df2= df1.to_numpy()
df3=df2.copy()

null_indexes = np.where(pd.isnull(df2))

# 打印空值的索引
a=[]  #行不变，列向前一个
for row, col in zip(null_indexes[0], null_indexes[1]):
    a.append((row,col))
    # print(f"空值的索引: 行 {row}, 列 {col}")
print(len(a))
for i in range(len(a)):
    try:
        if  df2[a[i][0], 0]:
            nan_x = df2[a[i][0], 0]
            nan_y = df2[0, a[i][1]]
            df3[a[i][0], a[i][1]] = IDW(know_lon, know_lat, know_z, nan_x, nan_y)
            print(a[i][0],a[i][1])
            print(df3[a[i][0], a[i][1]])
            pass
    except IndexError:
        # 处理索引超出边界的情况
        pass
df3 = pd.DataFrame(df3)
df3.to_excel('output.xlsx', index=False)










