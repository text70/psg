#! /usr/bin/env python

#######################################
# psg.py
#
# A script to tokenize your space-oriented files  
# to a single shotgun sequence of tokenized strings
#
# Author: <D.lee>
# Date: 08/26/2019
# Version: 1.0
#######################################

from nltk.tokenize import WhitespaceTokenizer, LineTokenizer, TabTokenizer
from pathlib import Path
import numpy as np

#Path.home = /home/my_username, thereforth , change the ''Data'/'PDB'/'2dpg.pdb' to your path of interest.
#use the pathlib read_text to open, read and close the file
p = Path.home()/'Data'/'PDB'/'2dpg.pdb'

s = p.read_text()
#Tokenize with whitespace
g = WhitespaceTokenizer().tokenize(s)
#Tokenize with lines
c = LineTokenizer(blanklines='discard').tokenize(s)
#Tokenize with tabs
d = TabTokenizer().tokenize(s)

x = [g, c, d]
print(np.ma.asarray([x]))

#if __name__ == '__main__':
    #main()
