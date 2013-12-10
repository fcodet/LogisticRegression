__author__ = 'frederic.codet'

from PlottingFunctions import *
from CostFunctions import *
import numpy as np
from scipy import optimize
from OptFunctions import *
from FileOps import *
from PlotDecisionBoundary import *

print('loading data...')
data = loadcsv('ex2data2.txt') #data is an array (m,n-1)
print('data loaded.')
col1 = np.array([data[:,0]]).transpose()
col2 = np.array([data[:,0]]).transpose()

vX = np.concatenate((col1, col2), 1)
vy = np.array([data[:, 2]]).transpose()
m = np.shape(vy)[0]
X = np.concatenate((np.ones((m, 1)), vX), 1)
y = vy

list_abs = data[:,0]
list_ord = data[:,1]
label = data[:,2]

x0_abs = []
x0_ord = []
x1_abs = []
x1_ord = []
for i in range(0,len(label)):
	if label[i]==1:
		x1_abs.append(list_abs[i])
		x1_ord.append(list_ord[i])
	else:
		x0_abs.append(list_abs[i])
		x0_ord.append(list_ord[i])
sets = [[x0_abs,x0_ord,'o','Microchip 1'],[x1_abs,x1_ord,'+','Microchip 2']]
#MultiScatter(sets)

X = mapFeature(data[:,0],data[:,1],6)

[m, n] = np.shape(X)
initial_theta  = np.zeros((n, 1))
lam = 1.0

#result_opt = optimize.fmin_cg((lambda theta: costReg(lam,theta,X,y)) , initial_theta,(lambda theta: gradReg(lam,theta,X,y)), maxiter = 10)
#result_opt = optimize.fmin_bfgs((lambda theta: costReg(lam,np.mat(theta).transpose(),X,y)) , np.array(initial_theta),(lambda theta: gradReg(lam,np.mat(theta).transpose(),X,y)), maxiter = 10)
#result_opt = optimize.fmin((lambda theta: costReg(lam,theta,X,y)) , initial_theta, full_output= True , maxiter = 1000)
result_opt = OptimizeF(initial_theta,lam, X ,y,300)
print result_opt
thetaf = result_opt[0]
plotDecisionBoundary(thetaf, X, y, sets)
