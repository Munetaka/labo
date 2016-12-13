import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets


# create random data
np.random.seed(0)
regdata = datasets.make_regression(100, 1, noise=20.0)


# plot data
plt.scatter(regdata[0], regdata[1])


# set model
model = linear_model.LinearRegression()
model.fit(regdata[0], regdata[1])

# plot regression line
x = [min(regdata[0]), max(regdata[0])]
plt.plot(x, model.coef_ * x + model.intercept_)

plt.show()
