__author__ = 'frederic.codet'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt

def Plot(x,y):
	ax = plt.axes()
	ax.scatter(x,y)
	plt.show()

def SurfacePlot(x,y,z):
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	x, y = np.meshgrid(x, y)
	ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	plt.show()

def MultiPlot(t, lines):
	ax = plt.axes()
	for line in lines:
		ax.plot(t,line)
	plt.show()

def MultiScatter(sets):
	ax = plt.axes()
	legendinfo = []
	colorinfo = []
	for set in sets:
		if len(set)>=4:
			legendinfo.append(set[3])
		else:
			legendinfo.append('')
		#ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),marker = set[2], label = legendinfo)
		ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),marker = set[2], label = legendinfo, c= set[4])
	ax.legend(legendinfo)
	plt.show()

def MultiScatter3D(sets):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    legendinfo = []
    colorinfo = []
    for set in sets:
        if len(set)>=4:
            legendinfo.append(set[3])
        else:
            legendinfo.append('')
        #ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),marker = set[2], label = legendinfo)
        ax.scatter(map(lambda xx: float(xx), set[0]),map(lambda xx: float(xx), set[1]),map(lambda xx: float(xx), set[2]),marker = set[3], label = legendinfo, c= set[5])
    ax.legend(legendinfo)
    plt.show()