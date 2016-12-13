from sklearn import svm, datasets, cross_validation

# load data
iris = datasets.load_iris()

# fit model
model = svm.SVC()
scores = cross_validation.cross_val_score(model, iris.data, iris.target, cv=5)

# result
print(scores)
print('accuracy:', scores.mean())
