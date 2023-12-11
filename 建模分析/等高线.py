import matplotlib.tri as tri
import matplotlib.pyplot as plt
import math
import js
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
df=pd.read_excel("2.xlsx")
lon=df.iloc[2:11485,0]
lon=np.array(lon)
lat = df.iloc[2:11485,1]
lat=np.array(lat)
z=df.iloc[2:11485,2]
z=np.array(z)

import numpy as np
import matplotlib.pyplot as plt

X, Y = np.meshgrid(lon, lat)

# 转换为二维数组
m = np.arange(len(z))
Z = z.reshape(X.shape)

# 绘制等高线图
plt.contour(X, Y, Z)

# 显示图形
plt.show()

# 绘制等高线图
plt.contour(X, Y, z)

# 添加颜色条
plt.colorbar()

# 显示图形
plt.show()