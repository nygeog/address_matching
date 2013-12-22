import os, csv

with open('data/data_01.csv','r') as csvinput:
    with open('data/data_02-temp.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('hn')
        all.append(row)

        for row in reader:
            row.append(row[1].split(' ')[0].lower().replace('.','').replace(',',''))
            all.append(row)

        writer.writerows(all)

with open('data/data_02-temp.csv','r') as csvinput:
    with open('data/data_02.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('street_etc')
        all.append(row)

        for row in reader:
            row.append(row[1].split(' ', 1)[1].lower().replace('.','').replace(',',''))
            all.append(row)

        writer.writerows(all)

os.remove('data/data_02-temp.csv')