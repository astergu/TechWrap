#coding=utf8

import pandas as pd

# header=0 indicates the first line of the file contains column names,
# delimiter indicates that the fields are separated by tabs,
# quoting=3 tells Python to ignore doubled quotes
train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter='\t', quoting=3)
print train.shape
print train.columns.values
print train["review"][0]

# import BeautifulSoup into your workspace
from bs4 import BeautifulSoup

# initialize the BeautifulSoup object on a single movie review
example1 = BeautifulSoup(train["review"][0])
print example1.get_text()