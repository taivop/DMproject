from helpers.datahandler import DataHandler
import numpy as np
import matplotlib.pyplot as plt


handler = DataHandler()
genders, ages, diagnoses = handler.removeAgesAbove100(handler.getAllData())

# --- Genders distribution ---
# 1 if male
print("Genders distribution")
print(genders.shape[0])
print("Men: {0}".format(sum(genders == 1)))
print("Women: {0}".format(sum(genders == 0)))

# --- Ages distribution ---
print("\nAges distribution")
# create histogram data for age distribution
bins = range(0,101,5)
hist, bins = np.histogram(ages, bins=bins)
print("Ages histogram values:")
[print("{0}".format(h)) for h in hist]
print("Ages bins:")
[print("{0}".format(b)) for b in bins]

# plot histogram (just to look at right now; will do it in some other program anyway)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
#plt.bar(center, hist, align='center', width=width)
#plt.show()



# --- Distribution of numbers of diagnoses ---
print("\nDiagnoses distribution")
summed = np.sum(diagnoses, axis=1)
bins = range(0,59,2)
hist, bins = np.histogram(summed, bins=bins)
print("Diagnosis histogram values:")
[print("{0}".format(h)) for h in hist]
print("Diagnosis bins:")
[print("{0}".format(b)) for b in bins]

# plot histogram (just to look at right now; will do it in some other program anyway)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()