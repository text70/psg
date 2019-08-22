from nltk.tokenize import WhitespaceTokenizer, LineTokenizer, TabTokenizer
from pathlib import Path
import numpy as np


p = Path.home()/'Data'/'PDB'/'2dpg.pdb'
#Path.home = /home/my_username, thereforth , change the ''Data'/'PDB'/'2dpg.pdb' to your path of interest.
#use the pathlib read_text to open, read and close the file
s = p.read_text()
#Tokenize with Whitespace
g = WhitespaceTokenizer().tokenize(s)
#print(g)
c = LineTokenizer(blanklines='discard').tokenize(s)
#print(c)
d = TabTokenizer().tokenize(s)

x = [g, c, d]
print(np.ma.asarray([x]))

#if __name__ == '__main__':
    #return()
