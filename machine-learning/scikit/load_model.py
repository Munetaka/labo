from sklearn import datasets
from sklearn.externals import joblib

# load datasets
iris = datasets.load_iris()

# load model from file
clf = joblib.load('clf.pkl') 

# result
print(clf.predict(iris.data))
