__author__ = 'frederic.codet'
from CostFunctions import *
from scipy import optimize

def OptimizeF(theta0, lam, X, y, iter):
    res = optimize.fmin_bfgs(CostF, theta0, GradF, args=(lam,X,y) , maxiter = iter)
    return res
