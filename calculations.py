import numpy as np
import scipy.optimize
np.seterr(all="ignore")

def sigmoid(z):
    sig = 1.0 / (1.0 + np.exp(-z))
    return sig

def predict(w, x):
    result = sigmoid(np.dot(w, x))
    print(str(result))
    if result > 0.5:
        return True
    else:
        return -1
    print(str(sigmoid(np.dot(w,x))))


def log_likelihood(X, Y, w, sigma):
    return np.sum(np.log(sigmoid(Y * np.dot(X, w)))) - (sigma/2) * np.dot(w, w)


def gradient(X, Y, w, sigma):
    attributes = len(w)
    entries = len(X)
    s = np.zeros(attributes)
    for i in range(entries):
        s += Y[i] * X[i] * sigmoid(-Y[i] * np.dot(X[i], w))
    s -= sigma * w
    return s


def gradient_numerical(X, Y, w, f, learning):
    num_attributes = len(w)
    ident = np.identity(num_attributes)
    h = np.zeros(num_attributes)
    for i in range(num_attributes):
        h[i] += f(X, Y, w + learning * ident[i])
        h[i] -= f(X, Y, w - learning * ident[i])
        h[i] /= 2 * learning
    return h


def correct(X, Y, w):
    total = 0
    for i in range(len(X)):
        if predict(w, X[i]) == Y[i]:
            total += 1
    return total * 1.0 / len(X)


def train(X, Y, sigma, learning):

    def f(w):
        return -(log_likelihood(X, Y, w, sigma))

    def fprime(w):
        return -(gradient(X,Y,w,sigma))

    num_entries = X.shape[1]
    initial_guess = np.zeros(num_entries, dtype=np.int64)

    w_vector = scipy.optimize.fmin_bfgs(f, initial_guess, fprime, gtol=.00001, disp=False)

    return w_vector

