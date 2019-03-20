import numpy as np
import pandas as pd

iris = pd.read_csv("./Iris.csv")
iris = iris.sample(frac=1).reset_index(drop=True) # Shuffle

print iris.head()

print "------------------------ Grab the data --------------------------"
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
X = np.array(X)
print X[:5]

from sklearn.preprocessing import OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse=False)

Y = iris.Species
print "_------------------------- Y -------------------"
print Y
Y = one_hot_encoder.fit_transform(np.array(Y).reshape(-1, 1))
print Y[:5]
