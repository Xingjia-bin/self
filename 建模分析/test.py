import math
import js
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
df=pd.read_excel("经纬度.xlsx")
know_lon=df.iloc[2:122,0]
know_lon=know_lon.tolist()
know_lat = df.iloc[0,1:123]
know_lat=know_lat.tolist()
know_z=df.iloc[2:122,1:123]

from shapely.geometry import Point, MultiPoint
# 创建经纬度坐标点
latitudes = know_lon
longitudes = know_lat
points = [Point(lon, lat) for lat, lon in zip(latitudes, longitudes)]
# 创建 MultiPoint 对象
multipoint = MultiPoint(points)
# 打印 MultiPoint 对象
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

    for p in range(len(xi)):
        lstdist = []
        for s in range(len(x)):
            d = (haversine(x[s], y[s], xi[p], yi[p]))
            lstdist.append(d)
        print(lstdist)
        sumsup = list((1 / np.power(lstdist, 2)))#权重
        suminf = np.sum(sumsup)#权重的和
        m=1
        z=df.iloc[2:122,m]
        z=np.array(z)
        # z=np.transpose(z)
        sumsup=np.array(sumsup)
        # sumsup=np.transpose(sumsup)
        sumsup = np.sum(sumsup * z)
        u = sumsup / suminf
        xyzi = [xi[p], yi[p], u]
        lstxyzi.append(xyzi)
    return(lstxyzi)


js_box = multipoint.bounds
#还是插入400*400的网格点
grid_lat = np.linspace(js_box[0],js_box[2],100)
grid_lon = np.linspace(js_box[1],js_box[3],100)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)
#将插值网格数据整理
df_grid =pd.DataFrame(dict(long=xgrid.flatten(),lat=ygrid.flatten()))
#这里将数组转成列表
grid_lon_list = df_grid["long"].tolist()
grid_lat_list = df_grid["lat"].tolist()

pm_idw = IDW(know_lon,know_lat,know_z,grid_lon_list,grid_lat_list)
IDW_grid_df = pd.DataFrame(pm_idw,columns=["lon","lat","idw_value"])
print(IDW_grid_df)
IDW_grid_df.head()
IDW_grid_df.to_excel('data.xlsx', index=False)



import plotnine
from plotnine import *
# plotnine.options.figure_size = (5, 4.5)
# idw_scatter = (ggplot() +
#            geom_map(df,fill='none',color='gray',size=0.4) +
#            geom_point(pm,aes(x='经度',y='纬度',fill='PM2.5'),size=5) +
#            scale_fill_cmap(cmap_name='Spectral_r',name='PM2.5',
#                            breaks=[30,40,60,80]
#                            )+
#            scale_x_continuous(breaks=[117,118,119,120,121,122])+
#            labs(title="Map Charts in Python Exercise 02: Map IDM point",
#                 )+
#            #添加文本信息
#            annotate('text',x=116.5,y=35.3,label="processed map charts with plotnine",ha="left",
#                    size=10)+
#            annotate('text',x=120,y=30.6,label="Visualization by DataCharm",ha="left",size=9)+
#            theme(
#                text=element_text(family="Roboto Condensed"),
#                #修改背景
#                panel_background=element_blank(),
#                axis_ticks_major_x=element_blank(),
#                axis_ticks_major_y=element_blank(),
#                axis_text=element_text(size=12),
#                axis_title = element_text(size=14,weight="bold"),
#                panel_grid_major_x=element_line(color="gray",size=.5),
#                panel_grid_major_y=element_line(color="gray",size=.5),
#             ))
# idw_scatter
#
#
# idw_scatter_inter = (ggplot() +
#            geom_tile(IDW_grid_df,aes(x='lon',y='lat',fill='idw_value'),size=0.1) +
#            geom_map(df,fill='none',color='gray',size=0.4) +
#            geom_point(pm,aes(x='经度',y='纬度',fill='PM2.5'),size=4,stroke=.3,show_legend=False) +
#            scale_fill_cmap(cmap_name='Spectral_r',name='idw_value',
#                            breaks=[30,40,60,80]
#                            )+
#            scale_x_continuous(breaks=[117,118,119,120,121,122])+
#            labs(title="Map Charts in Python Exercise 02: Map IDM point",
#                 )+
#            #添加文本信息
#            annotate('text',x=116.5,y=35.3,label="processed map charts with plotnine",ha="left",
#                    size=10)+
#            annotate('text',x=120,y=30.6,label="Visualization by DataCharm",ha="left",size=9)+
#            theme(
#                text=element_text(family="Roboto Condensed"),
#                #修改背景
#                panel_background=element_blank(),
#                axis_ticks_major_x=element_blank(),
#                axis_ticks_major_y=element_blank(),
#                axis_text=element_text(size=12),
#                plot_title=element_text(size=15,weight="bold"),
#                axis_title = element_text(size=14),
#                panel_grid_major_x=element_line(color="gray",size=.5),
#                panel_grid_major_y=element_line(color="gray",size=.5),
#             ))
# idw_scatter_inter