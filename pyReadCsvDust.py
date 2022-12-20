import csv
import glob
path = r'tables/*.csv'
files = glob.glob(path)
print(files)
dataFile = []
warning_points = 100 # print out a warning if found more than this value
for fname in files:
    data = []
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row['Area'])
    if len(data)>warning_points:
        print("warning: find more than 500 dusts, please check this file",fname)
            
    dataFile.append(data)

print(dataFile)
