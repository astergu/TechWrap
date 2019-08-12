# coding=utf8

import math


def rmse():
    """
    RMSE: Root Mean Square Error 均方根误差
    """
    return math.sqrt(sum([pow(ui - ti, 2) for ui, ti in records])) / len(records)


def mae():
    """
    MAE: Mean Absolute Error 平均绝对误差
    """
    return sum([abs(ui - ti) for ui, ti in records]) / len(records)
