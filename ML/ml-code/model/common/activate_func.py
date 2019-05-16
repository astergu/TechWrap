from math import exp


def sign(x):
    """
    sign function
    """
    return 1 if x >= 0.0 else -1

def sgn(x, center=0):
    if x >= center:
        return 1
    return 0


def sigmoid(x):
    """
    sigmoid function
    """
    return 1 / (1 + exp(-x))
