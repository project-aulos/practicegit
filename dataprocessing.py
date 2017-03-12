#!/usr/bin/python
# -*- coding : utf-8 -*-

import glob
import os
from os import listdir
from os.path import isfile, join
from os import walk
import sys

path = "/Users/jeonyongjin/desktop/Imagenetdataset"
dataset = "/Users/jeonyongjin/desktop/Imagenetdataset/dataset"

def allfiles(path):
    res = []

    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)
        print rootpath
        
        a = os.path.split(rootpath)
#        print a[0]
        print a[1]
        file_number = 0
        for file in files:
            
            filepath = os.path.join(rootpath, file)
            res.append(filepath)
    return res

filelist = allfiles(path)

if not os.path.exists(dataset):
    os.makedirs(dataset)

for fpath in filelist:
    f = os.path.split(fpath)
#    print f[0]
#    print f[1]
#    print f[2]
#    print f[3]
#    print f[4]
