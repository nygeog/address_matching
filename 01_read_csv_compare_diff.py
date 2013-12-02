import csv
import difflib #has Levenshtein distance

#wishlist:
#1 will want to split out house number at some point so it'll compare
#  the house number [ratio1] as well as the addess string[ratio2], hmmm, if ends in zip, 
#  maybe have a ratio3 for that as well. 

datafile = open('data_01.csv', 'r')
datareader = csv.reader(datafile, delimiter = ',')
headers = datareader.next()
data = []
for row in datareader:
    data.append(row)

# sub 0-9 to be 0 through count of items in list
for x in range(0, 9):
	y = data[x][1].lower().replace('.','').replace(',','')
	for compare in range(0, 9):
		z = data[compare][1].lower().replace('.','').replace(',','')
		print y + '^' + z
		print difflib.SequenceMatcher(None, y, z).ratio()

