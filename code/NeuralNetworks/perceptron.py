#coding=utf8

import sys
import numpy as np
from sklearn.linear_model import Perceptron as sk_perceptron

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self._eta = eta
        self._n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self._n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, x):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

if __name__ == '__main__':
    skp = sk_perceptron()
    skp.fit(X, y)
    #x = np.array([-2, 3, -1, 0])
    #p = Perceptron(size=4)
    #print p.binary_classifier(x)
