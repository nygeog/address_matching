import csv
import difflib #has Levenshtein distance

#wishlist:
#1 will want to split out house number at some point

datafile = open('data_01.csv', 'r')
datareader = csv.reader(datafile, delimiter = ',')
headers = datareader.next()
data = []
for row in datareader:
    data.append(row)

# sub 0-9 to be 0 through count of items in list
for x in range(0, 9):
	y = data[x][1].lower()
	for comp in range(0, 9):
		z = data[comp][1].lower()
		print y + '^' + z
		print difflib.SequenceMatcher(None, y, z).ratio()

