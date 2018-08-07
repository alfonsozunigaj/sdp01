import csv
import random

with open('5.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['ID','4G17V','FF21N','GOQP1','4G17V','FF21N','GOQP1','4G17V','FF21N','GOQP1','AA'])
    for i in range (100000):
        spamwriter.writerow([str(i),str(random.randint(1,10000)),str(random.randint(1,10000)),str(random.randint(1,10000)), str(random.randint(1,10000)), str(random.randint(1,10000)), str(random.randint(1,10000)), str(random.randint(1,10000)), str(random.randint(1,10000)), str(random.randint(1,10000))])