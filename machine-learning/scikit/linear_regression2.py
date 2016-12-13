import numpy as np
# import matplotlib.pyplot as plt
from sklearn import linear_model, datasets



# load data
diabetes = datasets.load_diabetes()


# separate data into for training and for predict
data_train = diabetes.data[:-20]
target_train = diabetes.target[:-20]
data_test = diabetes.data[-20:]
target_test = diabetes.target[-20:]

# fit model
model = linear_model.LinearRegression()
model.fit(data_train, target_train)


print("score :", model.score(data_test, target_test))
print("prediction :", model.predict(np.array(data_test[0]).reshape(1,-1)))
print("actual value :", target_test[0])
