import numpy as np
import matplotlib.pyplot as plt


class LinearRegression():

    def __init__(self, alpha, num_iters):
        self.alpha = alpha
        self.num_iters = num_iters

    def compute_cost(self, X, y, theta):
        return sum((X.dot(theta) - y) ** 2.) / (2. * y.size)

    def gradient_descent(self, X, y, theta):
        j_history = np.zeros(self.num_iters)
        for i in xrange(self.num_iters):
            theta = theta - self.alpha / y.size * X.T.dot(X.dot(theta) - y)
            j_history[i] = self.compute_cost(X, y, theta)

        self.j_history = j_history
        self.theta = theta
        return theta, j_history

    def plot_j_history(self):
        if self.j_history is None:
            print('no j_history exists')
            return
        plt.plot(np.arange(len(self.j_history)), self.j_history)
        plt.title('Convergence of gradient descent')
        plt.xlabel('No. of iterations')
        plt.ylabel('Cost function')
        plt.show()

    def plot_result(self, X, y):
        if self.theta is None:
            print('no result exists')
            return
        plt.plot(X[:,1].ravel(), y.ravel(), 'rx', label='Traning data')
        plt.plot(X[:,1].ravel(), X.dot(self.theta).ravel(), 'b', label="Linear Regression")
        plt.title('Training data with linear regression fit')
        plt.legend()
        margin = 1
        plt.xlim(X.min() - margin, X.max() + margin)
        plt.ylim(y.min() - margin, y.max() + margin)
        plt.show()


