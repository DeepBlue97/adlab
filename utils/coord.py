"""
坐标系之间的转换：
车架坐标系和传感器坐标系之间的坐标转换。
"""

import math


def get_rotation_matrix():
    """
    获得旋转矩阵，是在乘以该矩阵时改变向量的方向但不改变大小。
    """
    pass


def transform_coord2d(origin, alpha, object_coord):
    """
    args:
        origin: (X0,Y0) 局部坐标原点在全局坐标中的位置
        alpha: 局部坐标系相对于全局坐标系的旋转弧度，逆时针方向为正方向
        object_coord: (x1,y1) 目标点在局部坐标系中的位置

    return:
        X1,Y1: 目标点在全局坐标系中的坐标
    """
    X0, Y0 = origin
    x1, y1 = object_coord
    l1 = math.sqrt(x1**2 + y1**2)

    theta = math.asin(x1/l1)

    X2 = math.cos(theta-alpha) * l1 + X0
    Y2 = math.sin(theta-alpha) * l1 + Y0

    return X2, Y2
