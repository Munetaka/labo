import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

from sigmoid import sigmoid as sigmoid
from map_feature import mapFeature


class LogisticRegression():

    def __init__(self, alpha, num_iters):
        self.alpha = alpha
        self.num_iters = num_iters

    def compute_cost(self, theta, X, y, lam = 0):
        def safe_log(x, minval=0.0000000001):
            return np.log(x.clip(min=minval))
        h_theta = sigmoid(X.dot(theta))
        j = 1. / y.size * np.sum(-y * safe_log(h_theta) - (1 - y) * safe_log(1 - h_theta)) + lam / (2 * y.size) * np.sum(theta[1:] ** 2)
        return j

    def compute_grad(self, theta, X, y, lam = 0.):
        h_theta = sigmoid(X.dot(theta))
        grad = 1. / y.size * X.T.dot(h_theta - y)
        print('before')
        print(grad)
        grad[1:] = grad[1:] + (lam / y.size) * theta[1:]
        print('after')
        print(grad)
        return grad

    def gradient_descent(self, theta, X, y, lam):
        j_history = np.zeros(self.num_iters)
        for i in xrange(self.num_iters):
            theta = theta - self.alpha * self.compute_grad(theta, X, y, lam)
            j_history[i] = self.compute_cost(theta, X, y, lam)

        self.theta = theta
        self.j_history = j_history
        return theta, j_history

    def conjugate_descent(self, theta, X, y, lam = 0.):
        theta = optimize.fmin_cg(self.compute_cost, theta, fprime=self.compute_grad, args=(X, y.ravel(), lam))
        self.theta = theta
        return theta

    def plot_j_history(self):
        if self.j_history is None:
            print('no history exists')
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
        pos = np.where(y == 1)[0]
        neg = np.where(y == 0)[0]
        plt.plot(X[pos,1], X[pos,2], 'k+', label='Admitted')
        plt.plot(X[neg,1], X[neg,2], 'yo', label='Not Admitted')
        predict_x = np.array([X[:,1].min(), X[:,1].max()])
        predict_y = (-1. / self.theta[2]) * (self.theta[1] * predict_x + self.theta[0])
        plt.plot(predict_x, predict_y, 'b', label="Linear Regression")
        plt.legend()
        plt.title('Training data with linear regression fit')
        plt.show()

    def plot_result_with_featuremap(self, X, y):
        if self.theta is None:
            print('no result exists')
            return
        pos = np.where(y == 1)[0]
        neg = np.where(y == 0)[0]
        plt.plot(X[pos,1], X[pos,2], 'k+', label='Admitted')
        plt.plot(X[neg,1], X[neg,2], 'yo', label='Not Admitted')
        predict_x = np.array([X[:,1].min(), X[:,1].max()])
        plt.legend()
        plt.title('Training data with logistic regression fit')

        # prot disition boundary
        gridsize = 100
        x1_vals = np.linspace(20, 100, gridsize)
        x2_vals = np.linspace(20, 100, gridsize)
        x1_vals, x2_vals = np.meshgrid(x1_vals, x2_vals)
        z = np.zeros((gridsize, gridsize))
        for i in range(gridsize):
            for j in range(gridsize):
                x1 = np.array([x1_vals[i, j]])
                x2 = np.array([x2_vals[i, j]])
                z[i, j] = np.dot(mapFeature(x1, x2), self.theta)

        print(z)
        plt.contour(x1_vals, x2_vals, z, levels=[0])
        plt.xlabel("x1")
        plt.ylabel("x2")
        # plt.xlim((-1, 1.5))
        # plt.ylim((-1, 1.5))
        plt.show()
