__author__ = 'benjaminreis'

 # import libraries
import csv as csv
import numpy as np

# reads through the csv file and stores them as a list of strings in the csv_file_object
csv_file_object = csv.reader(open('csv/train.csv', 'rb'))

 #skip the first row of the csv file, its a header row next()
header = csv_file_object.next()


#loop through the csv object and store everything in a data variable
data=[]
for row in csv_file_object:
    data.append(row)
data = np.array(data) #convert the list to an array

print data  # spit it out to the console!