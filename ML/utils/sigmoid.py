#coding=utf8

import sys
import math
import numpy as np


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_vec(x):
    if isinstance(x, list):
        x = np.array(x)
        
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    s = sigmoid_vec(x)
    ds = np.multiply(s, 1 - s)
    return ds


if __name__ == '__main__':
    ret = sigmoid_derivative(np.array([1, 2, 3]))
    #ret = sigmoid_vec([1, 2, 3])
    print(ret)