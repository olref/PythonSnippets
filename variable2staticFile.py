#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# a little piece of code to transform a variable line size file into
# a fixed line size file (mainly used with old languages like cobol)
#

fixedSize = 2000

#open output file
f = open('outpath', 'w')

for line in open('inputpath'):
    lineOut = line.replace("\n","") #first remove current line feed
    lineOut = lineOut.ljust(fixedSize) + '\n' #add and spaces and line feed
    f.write(lineOut)
    
f.close()





