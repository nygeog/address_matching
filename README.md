Address Matching
================

Code to match address strings from a large set using Levenshtein, in R and/or Python. 

Notes
=====

1) So one thing to consider is to create seperate ratios for address house number first, then address (suffix, prefix, state, etc and then maybe a 3rd for ZIP. Because the score of 50 Main St. compared to 59 Main St. will be really close and these are inherently different.

May want to split the string of the house number out, assign some weight or value to it. 

http://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python

R
==
http://stat.ethz.ch/R-manual/R-devel/library/utils/html/adist.html
Python
======
http://www.coli.uni-saarland.de/courses/LT1/2011/slides/Python-Levenshtein.html
https://code.google.com/p/pylevenshtein/

USES THIS

http://stackoverflow.com/questions/6690739/fuzzy-string-comparison-in-python-confused-with-which-library-to-use

Wikipedia
=========
http://en.wikipedia.org/wiki/Levenshtein_distance


