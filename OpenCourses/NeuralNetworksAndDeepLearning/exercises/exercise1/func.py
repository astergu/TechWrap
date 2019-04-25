#coding=utf8

from __future__ import print_function
import numpy as np


def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """
    s = 1 / (1 + np.exp(-z))
    return s


if __name__ == '__main__':
    print ("sigmoid(0) = " + str(sigmoid(0)))
    print ("sigmoid(9.2) = " + str(sigmoid(9.2)))
