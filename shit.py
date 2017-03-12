#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle as pickle
import numpy as np
from PIL import Image
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt

def loading(filename):
	with open(filename, 'r') as f:
		datadict = pickle.load(f)
		print datadict
		x = datadict['data']
	return x

x = loading('data_batch_1')

print x
# print x[0].size

for i in range(0, 10):
#	print x[i]
	img = x[i]
#	img1 = Image.fromarray(img, 'RGB')
	img = np.array(img, dtype=np.uint8)
	img = np.reshape(img,(32,32,3))
#	img1 = Image.fromarray(img, 'RGB')
#	img = Image.fromarray(img)
	img = Image.fromarray(np.uint8(cm.gist_earth(img)*255))	

	print img1
	print img[i,i]
	imsave('%d.jpg'%i , img1)
	img1.show()
