data_file = '../data/age_predict_data.txt'

import numpy as np
data = np.loadtxt(data_file,delimiter='\t', skiprows=161439, dtype={'names': ('gender', 'age', 'diagnoses', 'prescriptions'),'formats': ('S1', 'i3', 'object', 'object')})
# loaded data starting on the 161439-th row, loaded 'diagnoses' and 'prescriptions' fields as Python string objects, not numpy string fields

print(data)