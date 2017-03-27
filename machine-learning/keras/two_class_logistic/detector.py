import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn import preprocessing
# import matplotlib.pyplot as plt


# load training data
data = np.genfromtxt('data.txt', delimiter=',')
X = data[:, (0, 1)]
t = data[:, 2]


# normalize data
X = preprocessing.scale(X)


# plot training data
# def plot_data(X, t):
#     positive = [i for i in range(len(t)) if t[i] == 1]
#     negative = [i for i in range(len(t)) if t[i] == 0]
#     plt.scatter(X[positive, 0], X[positive, 1], c='red', marker='o', label='positive')
#     plt.scatter(X[negative, 0], X[negative, 1], c='blue', marker='o', label='negative')
# plt.figure(1)
# plot_data(X, t)


# create the logistic regression model
model = Sequential()
model.add(Dense(1, input_shape=(2, )))
model.add(Activation('sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# fit the model
model.fit(X, t, nb_epoch=1000, batch_size=5, verbose=1)


# evaluate the model
scores = model.evaluate(X, t)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
print(model.metrics_names)
print(scores)
