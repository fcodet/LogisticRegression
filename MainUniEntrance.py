__author__ = 'frederic.codet'

from PlottingFunctions import *
from CostFunctions import *
import numpy as np
from scipy import optimize
from OptFunctions import *
from FileOps import *
from PlotDecisionBoundary import *

print('loading data...')
data = loadcsv('binary.csv') #data is an array (m,n-1)
print('data loaded.')
col1 = np.array([data[:,0]]).transpose()  #GRE
col2 = np.array([data[:,1]]).transpose()  #GPA
col3 = np.array([data[:,2]]).transpose()  #Rank

vX = np.concatenate((col2, col3), 1)
vX = np.concatenate((col1, vX), 1)
vy = np.array([data[:, 3]]).transpose()
m = np.shape(vy)[0]
X = np.concatenate((np.ones((m, 1)), vX), 1) #vX columns of 1,x0,x1,x2
y = vy

list_abs = data[:,1]
list_ord = data[:,2]
label = data[:,3]

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
sets = [[x0_abs,x0_ord,'o','Fail'],[x1_abs,x1_ord,'+','Admit']]
MultiScatter(sets)
