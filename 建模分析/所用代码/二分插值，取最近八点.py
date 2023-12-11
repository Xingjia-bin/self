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

    lstdist = []
    for s in range(len(x)):
        d = (haversine(x[s], y[s], xi, yi))
        lstdist.append(d)

    sumsup = list((1 / np.power(lstdist, 2)))#权重
    suminf = np.sum(sumsup)#权重的和
    z=np.array(z)
    sumsup=np.array(sumsup)
    sumsup = np.sum(sumsup * z)
    u = sumsup / suminf
    xyzi = [u]
    lstxyzi.append(xyzi)
    return u


# 两个一维数组
array1 = np.array(know_lon)
array2 = np.array(know_lat)

# 使用 reshape() 函数将两个数组转换为所需形式
result = np.vstack((array1, array2)).T

known_points = np.array(result)
known_points = np.around(known_points, decimals=4)
df1 = pd.read_excel('123.xlsx')
df2= df1.to_numpy()
df2= np.around(df2, decimals=4)
df3=df2.copy()

for i in range(1,241,1):
    for j in range (1,245,1):
        given_point = [df2[i][0],df2[0][j]]
        # 使用 np.where() 判断子数组是否在原始数组中，并返回索引值
        indices = np.where((known_points == given_point).all(axis=1))[0]

        if  len(indices)!=0:#判断是否在原有数据内
            df3[i][j]=know_z[indices[0]]#zai
        else:
            distances = np.linalg.norm(known_points - given_point, axis=1)
            closest_indices = np.argsort(distances)[:8]
            print(closest_indices)
            list1=[]
            for m in range(8):
                list1.append(know_z[closest_indices[m]])
            closest_points = known_points[closest_indices]
            x=closest_points[:,0]
            y=closest_points[:,1]
            # z=know_z[closest_indices]
            # print(closest_points)
            df3[i][j]=IDW(x,y,list1,df2[i][0],df2[0][j])
df3 = pd.DataFrame(df3)
df3.to_excel('456.xlsx', index=False)








# given_point = np.array([115.01665, 11.0068])

# 计算每个已知点与给定点之间的欧氏距离
# distances = np.linalg.norm(known_points - given_point, axis=1)
#
# # 获取距离最近的八个点的索引
# closest_indices = np.argsort(distances)[:8]
#
# # 提取距离最近的八个点的坐标
# closest_points = known_points[closest_indices]
#
# # 打印最相近的八个已知点的坐标
# print(closest_points)

# xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)
#将插值网格数据整理
# df_grid =pd.DataFrame(dict(long=xgrid.flatten(),lat=ygrid.flatten()))
#这里将数组转成列表
# grid_lon_list = df_grid["long"].tolist()
# grid_lat_list = df_grid["lat"].tolist()
# ycx=
# ycy=
#
# pm_idw = IDW(know_lon,know_lat,know_z,ycx,ycy)
# IDW_grid_df = pd.DataFrame(pm_idw,columns=["lon","lat","idw_value"])
# print(IDW_grid_df)
# IDW_grid_df.head()
# IDW_grid_df.to_excel('二分.xlsx', index=False)
#


