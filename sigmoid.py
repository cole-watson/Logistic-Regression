import numpy as np

def sigmoid(z):
	return (1/(1 + exp(-z)))

def predict(w, x):
	return sigmoid(np.dot(w,x)) > 0.5 or 1