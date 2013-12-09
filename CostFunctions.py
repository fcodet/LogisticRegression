__author__ = 'frederic.codet'

import numpy as np


def sigmoid(z):
	#z can be a scalar, array - vector or array - matrix
	#the sigmoid function will be applied to each of its elements
	sig = 1.0 / ( 1.0 + np.exp(-z) )
	return sig

def CostF(theta,lam , X, y):
	#theta is a (n,1) vector
	#X is a (m,n) matrix
	#y is a (m,1) vector
	m = np.shape(y)[0]
	n = np.shape(theta)[0]
	J = 0.0
	thetat = theta.transpose() #thetat is a (1,m) vector
	for i in range(0,m):
		Xit = X[i, :].transpose() #Xit is (n,1) vector
		if y[i]==1:
			print thetat
			print Xit
			print(np.dot(thetat,Xit))

			J = J + 1.0/ m * ( -y[i] * np.log(sigmoid(np.dot(thetat,Xit))))
		else:
			J = J + 1.0/ m * (-(1 - y[i]) * np.log(1-sigmoid(np.dot(thetat,Xit))))
	for j in range(1, n):
		J = J + lam / (2*m) *theta[j]**2
	print J
	return J

def GradF(theta,lam, X, y):
	#theta is a (n,1) vector
	#X is a (m,n) matrix
	#y is a (m,1) vector
	m = np.shape(y)[0]
	n = np.shape(theta)[0]
	grad = np.zeros(np.shape(theta))
	thetat = theta.transpose() #thetat is a (1,m) vector
	for j in range(0, n):
		for i in range(0, m):
			if (j!=0):
				grad[j] = grad[j] + lam/(2*m)*theta[j]**2
			Xit = X[i, :].transpose() #Xit is (n,1) vector
			grad[j] = grad[j] + 1.0 / m * (sigmoid(np.dot(thetat,Xit))-y[i])* X[i,j]

	return grad

def mapFeature(X1,X2,degree):
	#X1 is a (m,1) array - matrix
	#X2 is a (m,1) array - matrix
	m = np.shape(X1)[0]
	X = np.ones((m, 1)) #X starts with a vector (m,1) of 1s
	for i in range(1,degree+1):
		for j in range(0,i+1):
			temp = np.zeros((m,1))
			for k in range(0,m):
				temp[k] = X1[k]**(i-j) * X2[k]**j
			X = np.concatenate((X,temp), 1) #Add an extra column of features (m,1) until all degrees run out
	return X
