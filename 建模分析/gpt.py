import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf
import math
import js
from math import radians, cos, sin, asin, sqrt
import pandas as pd
df=pd.read_excel("经纬度.xlsx")
know_lon=df.iloc[2:122,0]
know_lon=know_lon.tolist()
know_lat = df.iloc[0,1:123]
know_lat=know_lat.tolist()
know_z=df.iloc[2:122,1:123]
# 构造样点数据
from shapely.geometry import Point, MultiPoint
# 创建经纬度坐标点
latitudes = know_lon
longitudes = know_lat
points = [Point(lon, lat) for lat, lon in zip(latitudes, longitudes)]
# 创建 MultiPoint 对象
multipoint = MultiPoint(points)
js_box = multipoint.bounds
#还是插入400*400的网格点
grid_lat = np.linspace(js_box[0],js_box[2],20)
grid_lon = np.linspace(js_box[1],js_box[3],20)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)
#将插值网格数据整理
df_grid =pd.DataFrame(dict(long=xgrid.flatten(),lat=ygrid.flatten()))
#这里将数组转成列表
grid_lon_list = df_grid["long"].tolist()
grid_lat_list = df_grid["lat"].tolist()
# 计算插值结果
rbf = Rbf(know_lon, know_lat , know_z, function='inverse')
zi = rbf(grid_lon_list , grid_lat_list)

# 绘制示意图
plt.imshow(zi, cmap='rainbow', extent=(js_box[0], js_box[2], js_box[1], js_box[3]))
plt.colorbar()
plt.scatter(know_lon, know_lat, c=know_z, cmap='rainbow', edgecolors='black', linewidths=1)
plt.title('Inverse Distance Weighting Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
