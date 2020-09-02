with open ('data.csv',)as f:
    for line in f:
        print(line)

import csv
with open('data.csv',encoding="utf-8")as f:
    for line in csv.reader(f):
        print(line)