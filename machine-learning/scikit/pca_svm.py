from sklearn import datasets
from sklearn import svm
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt



# load data
iris = datasets.load_iris()


# transform by PCA
pca = PCA(n_components=2)
data = pca.fit(iris.data).transform(iris.data)


# create mesh
datamax = data.max(axis=0) + 1
datamin = data.min(axis=0) - 1
n = 200
X, Y = np.meshgrid(
        np.linspace(datamin[0], datamax[0], n),
        np.linspace(datamin[1], datamax[1], n)
        )


# fit model
svc = svm.SVC()
svc.fit(data, iris.target)
Z = svc.predict(np.c_[X.ravel(), Y.ravel()])


# plot
# plt.contour(X, Y, Z.reshape(X.shape), colors='k')
# plt.contour(X, Y, Z.reshape(X.shape))
plt.contourf(X, Y, Z.reshape(X.shape))
for c, s in zip([0, 1, 2], ['o', '+', 'x']):
    d = data[iris.target == c]
    plt.scatter(d[:,0], d[:,1], c='k', marker=s)
plt.show()
