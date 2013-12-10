__author__ = 'frederic.codet'
__author__ = 'frederic.codet'
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from CostFunctions import *
from PlottingFunctions import *

def PlotDecisionUni(theta, X, y, sets):
    ax = plt.axes()
    legendinfo = []
    colorinfo = []
    for set in sets:
        if len(set)>=4:
            legendinfo.append(set[3])
        else:
            legendinfo.append('')
            #ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),marker = set[2], label = legendinfo)
        ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),marker = set[2], label = legendinfo)#, c= set[4])
    ax.legend(legendinfo)

    u = np.linspace(-2,2,50)
    v = np.linspace(-2,2,50)

    z = np.zeros((len(u),len(v)))

    for i in range(0,len(u)):
        for j in range(0,len(v)):
            temp_array = mapFeature(np.array([[u[i]]]),np.array([[v[j]]]),5)
            temp_array = np.concatenate((temp_array,[[4.0]]),1)
            z[i,j] = np.dot( temp_array  , np.array(theta).transpose())
            #z[i,j] = np.dot( np.array([1.0, u[i], v[j], 3.0])  , np.array(theta).transpose())
		    #z[i,j] = np.dot (mapFeature(np.array([[u[i]]]),np.array([[v[j]]]),6) , np.array(theta).transpose())
	print(z)
    manual_locations = [(-1, 1)]
    #CS = plt.contour(u, v, z, fontsize=10 , manual = manual_locations)
    cs = plt.contourf(u, v, z, hatches=['-', '/', '\\', '//'],cmap=plt.get_cmap('gray'),extend='both', alpha=0.5)

    plt.colorbar()




    plt.show()
    print('done...finally')