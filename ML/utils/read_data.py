#coding=utf8

import os
import sys

IRIS_DATA = "../datasets/iris/iris.data"

def read_iris():
    with open(IRIS_DATA) as fp:
        for line in fp:
            print line.strip()

if __name__ == '__main__':
    read_iris()
