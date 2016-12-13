import numpy as np
from sklearn import linear_model, datasets, cross_validation


# load data
iris = datasets.load_iris()

# select 2 kinds of iris
data = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

# shuffle data
rng = np.random.RandomState(0)
permutation = rng.permutation(len(data))
data, target = data[permutation], target[permutation]


# fit model
model = linear_model.LogisticRegression()
scores = cross_validation.cross_val_score(model, data, target, cv=5)


# result
print(scores)
