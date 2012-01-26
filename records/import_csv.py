import csv
reader = csv.reader(open('programming-sample.tab', 'rb'))
for index,row in enumerate(reader):
    print 'Record: ' + str(index + 1)
    print '------------'
    print 'Title: ' + row[0]
    print 'Month: ' + row[1]
    print 'Day: ' + row[2]
    print 'Body: ' + row[3]
