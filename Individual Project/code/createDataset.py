import numpy
from numpy import genfromtxt

#Read in the file to an array
filename = 'smallDataset.txt'
dataset = genfromtxt(filename, delimiter=',', dtype=int)

numpy.random.shuffle(dataset)

training, testing = dataset[:8,:], dataset[8:,:]

numpy.savetxt('training.txt', training, fmt='%1d', delimiter=',', newline='\n')
numpy.savetxt('testing.txt', testing, fmt='%1d', delimiter=',', newline='\n')
