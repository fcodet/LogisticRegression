__author__ = 'frederic.codet'
import numpy as np

def loadcsv(fn):
	f = open(fn)
	lines = f.readlines()
	lines = map(lambda(x): x.strip('\n'), lines)
	lines = map( lambda(x): x.split(','), lines)
	lines = map( lambda(x): map( lambda(y): float(y), x),lines)
	return_array = np.asarray(lines)
	return (return_array)
