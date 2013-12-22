import csv
import difflib #has Levenshtein distance

#wishlist:
#1 will want to split out house number at some point so it'll compare
#  the house number [ratio1] as well as the addess string[ratio2], hmmm, if ends in zip, 
#  maybe have a ratio3 for that as well. 

datafile = open('data/data_02.csv', 'r')
datareader = csv.reader(datafile, delimiter = ',')
headers = datareader.next()
print datareader

data = []
for row in datareader:
    data.append(row)


print data 
ratiodata = []
# figure out how to write this file to a csv to create a matrix
#for ratRow i
# sub 0-9 to be 0 through count/length of items in list
#print data

for x in range(0, 9):
	y = data[x][3]
	for compare in range(0, 9):
		z = data[compare][3]
		print y + '^' + z
		ratioVal = difflib.SequenceMatcher(None, y, z).ratio()
		print ratioVal
		#data.append(ratioVal)

# print data
# print ratiodata