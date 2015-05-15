import os
import numpy as np

def obtenerDictPage():
	listOfFiles = os.listdir("pages")[1:]
	dictPages  = {}
	stringToSearch = '<a href="http://'
	for page in listOfFiles:
		dictPages[page] = []
		f = open("pages/%s"%page)
		
		for linea in f.readlines():
			while linea != None:
				posApertura = linea.find(stringToSearch)

				if posApertura == -1:
					linea = None
				else:
					linea = linea[posApertura + len(stringToSearch) :]
					posCierre = linea.find('">')
					url = linea[:posCierre]
					#print url
					dictPages[page].append(url)
					linea = linea[posCierre:]
		f.close()
	return dictPages

def pageRank(dictLinks):
 	fnames = ['angelinajolie.html', 'bradpitt.html',
			'jenniferaniston.html', 'jonvoight.html',
			'martinscorcese.html', 'robertdeniro.html']

	mapToNumbers = dict([(v,i) for i,v in enumerate(fnames)])
	lenKeysDict = len(fnames)
	T = np.zeros((lenKeysDict,lenKeysDict))
	for page in fnames:
		indexPage = mapToNumbers[page]
		linkToPage = dictLinks[page]
		for linkPage in linkToPage:
			indexLinkPage = mapToNumbers[linkPage]
			T[indexPage][indexLinkPage] += 1
	
	epsilon = 0.01
	E = (np.ones((lenKeysDict,lenKeysDict))/lenKeysDict) * epsilon
	L = T + E
	'''sumLByRow = np.sum(L,axis=1) #axis=1 means By Row
	G = L/sumLByRow
	return L,G,sumLByRow'''
	G = np.matrix(np.zeros(L.shape))
	for i in xrange(lenKeysDict):
		G[i,:] = L[i,:] / np.sum(L[i,:])
	return G