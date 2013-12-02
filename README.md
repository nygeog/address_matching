Address Matching
================

Code to match address strings from a large set using Levenshtein, in R and/or Python. 

Notes
=====

1) So one thing to consider is removing the address house number first and then add it later. Because the score of 50 Main St. compared to 59 Main St. will be really close and these are inherently different


R
==
http://stat.ethz.ch/R-manual/R-devel/library/utils/html/adist.html
Python
======
http://www.coli.uni-saarland.de/courses/LT1/2011/slides/Python-Levenshtein.html
https://code.google.com/p/pylevenshtein/

Wikipedia
=========
http://en.wikipedia.org/wiki/Levenshtein_distance


