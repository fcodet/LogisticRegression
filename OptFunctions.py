__author__ = 'frederic.codet'
from CostFunctions import *
from PlottingFunctions import *
from scipy import optimize

def OptimizeF(theta0, lam, X, y, iter):
	#res = optimize.fmin_cg(CostF, theta0, GradF, args=(lam,X,y), maxiter = iter, full_output=True,retall=True)
	#res = optimize.fmin_ncg(CostF, theta0, GradF, args=(lam,X,y) , maxiter = iter,full_output=True,retall=True)
	#res = optimize.fmin_cg(CostF, theta0, None, args=(lam,X,y) , maxiter = iter)
	res = optimize.fmin_bfgs(CostF, theta0, GradF, args=(lam,X,y) , maxiter = iter,full_output=True,retall=True)
	its = range(0,len(res[7]))
	J_history = np.zeros((len(res[7]),))
	for i in range(0,len(res[7])):
		J_history[i] = CostF( res[7][i] ,lam, X, y)
	Plot(its,J_history)
	return res
