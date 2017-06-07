from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

# fit SVM model
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# result
print(clf.predict(X))

# serialize model
joblib.dump(clf, 'clf.pkl') 
