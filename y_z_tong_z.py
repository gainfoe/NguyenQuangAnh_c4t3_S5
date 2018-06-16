from math import *

def y_z_tong_z(x):
    y = []
    z = []
    sum_z = 0
    for i in range(len(x)):
        y.append(round(pi/2 - x[i], 2))
        z.append(round(cos(x[i]) - sin(x[i]), 2))
        sum_z += cos(x[i]) - sin(x[i])
    return y, z, sum_z