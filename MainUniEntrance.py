__author__ = 'frederic.codet'

from PlottingFunctions import *
from CostFunctions import *
import numpy as np
from scipy import optimize
from OptFunctions import *
from FileOps import *
from PlotDecisionUni import *

print('loading data...')
data = loadcsv('binary.txt') #data is an array (m,n-1)
print('data loaded.')
col1 = np.array([data[:,1]]).transpose()  #GRE
col2 = np.array([data[:,2]]).transpose()  #GPA
col3 = np.array([data[:,3]]).transpose()  #Rank

col1 = (col1 - np.mean(col1))/np.std(col1)
col2 = (col2 - np.mean(col2))/np.std(col2)


vX = np.concatenate((col2, col3), 1)
vX = np.concatenate((col1, vX), 1)
vy = np.array([data[:, 0]]).transpose()
m = np.shape(vy)[0]
X = np.concatenate((np.ones((m, 1)), vX), 1) #vX columns of 1,x0,x1,x2
y = vy




list_abs = col1 #data[:,0]
list_ord = col2 #data[:,1]
list_vert = col3 #data[:,2]
label = y #data[:,3]

x0_abs = []
x0_ord = []
x0_vert = []
x1_abs = []
x1_ord = []
x1_vert = []

for i in range(0,len(label)):
    #if ((label[i]==1) and (list_vert[i]==4)):
    if (label[i]==1):
        x1_abs.append(list_abs[i])
        x1_ord.append(list_ord[i])
        x1_vert.append(list_vert[i])
    else:
        x0_abs.append(list_abs[i])
        x0_ord.append(list_ord[i])
        x0_vert.append(list_vert[i])
sets = [[x0_abs,x0_ord,'+','Fail','red'],[x1_abs,x1_ord,'o','Admit','blue']]
#sets = [[x1_abs,x1_ord,'+','Admit','red']]
MultiScatter(sets)
sets3D = [[x0_abs,x0_ord,x0_vert,'+','Fail','red'],[x1_abs,x1_ord,x1_vert,'o','Admit','blue']]
MultiScatter3D(sets3D)

X = mapFeature(col1,col2,5)
X = np.concatenate((X, col3), 1)

[m, n] = np.shape(X)
initial_theta  = np.zeros((n, 1))
lam = 1.0

#result_opt = optimize.fmin_cg((lambda theta: costReg(lam,theta,X,y)) , initial_theta,(lambda theta: gradReg(lam,theta,X,y)), maxiter = 10)
#result_opt = optimize.fmin_bfgs((lambda theta: costReg(lam,np.mat(theta).transpose(),X,y)) , np.array(initial_theta),(lambda theta: gradReg(lam,np.mat(theta).transpose(),X,y)), maxiter = 10)
#result_opt = optimize.fmin((lambda theta: costReg(lam,theta,X,y)) , initial_theta, full_output= True , maxiter = 1000)
result_opt = OptimizeF(initial_theta,lam, X ,y,300)
print result_opt
thetaf = result_opt[0]
PlotDecisionUni(thetaf, X, y, sets)

