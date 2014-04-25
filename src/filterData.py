# This script filters from the data all patients who have no diagnoses or no prescriptions.
# Uses a for-loop but is pretty fast even with the whole dataset (couple of seconds) so it doesn't matter.

data_file = '../data/age_predict_data.txt'

import numpy as np
data = np.loadtxt(data_file,delimiter='\t', skiprows=161430, dtype={'names': ('gender', 'age', 'diagnoses', 'prescriptions'),'formats': ('S1', 'i3', 'object', 'object')})
# loaded data starting from the 161430-th row, loaded 'diagnoses' and 'prescriptions' fields as Python string objects, not numpy string fields

# keep track of rows that we want to keep in this list
toBeKept = []

for ii in range(1,len(data)):
    row = data[ii]
    # if both diagnoses and prescriptions exist, keep the row
    if(row[2] != "b'NONE'" and row[3] != "b'NONE'"):
        toBeKept.append(ii)


filtered = data[toBeKept]
print("filtered")
#print(filtered)