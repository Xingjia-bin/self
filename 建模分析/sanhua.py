import numpy as np

data = A
station = B
m, n = station.shape
lon = np.zeros(m)
lat = np.zeros(m)

for i in range(m - 1):
    lon[0] = station[0, 0] - (station[1, 0] - station[0, 0]) / 2
    lat[0] = station[0, 1] - (station[1, 1] - station[0, 1]) / 2
    lon[i + 1] = (station[i, 0] + station[i + 1, 0]) / 2
    lat[i + 1] = (station[i, 1] + station[i + 1, 1]) / 2

e = 2
num = 14
n1, n2 = lon.shape
n3, n4 = data.shape
x = station[:, 0]
y = station[:, 1]
z = data

for i1 in range(n1):
    X = lon[i1]
    Y = lat[i1]
    t1 = len(x)
    t2 = len(X)

    if t1 != 0 and t2 != 0:
        for j in range(t2):
            r = np.sqrt((X[j] - x) ** 2 + (Y[j] - y) ** 2) ** e
            I = np.argsort(r)
            m = len(I)

            if m > num:
                R = I[:num]
                z11 = z[:, J]
                z1 = z11[:, :num]
            else:
                print('数据量不足')
                break

            a = np.sum(z1 / np.tile(R, (n3, 1)), axis=1)
            b = np.sum(1 / R)
            Z[:, j] = a / np.tile(b, (n3, 1))