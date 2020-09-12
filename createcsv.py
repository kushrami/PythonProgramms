#There is csv library. to do all the fun stuff import csv.

import csv

filename = "Test.csv"
accessmode = "w+"

file = open(filename, mode = accessmode)

file.write("kush,26\n")
file.write("shweta,31")

file.close()
with open (filename, mode = 'r') as mytestfile:
    datafromfile = csv.reader(mytestfile)
    for currentrow in datafromfile:
        print(','.join(currentrow))
        for currentname in currentrow:
            print(currentname)