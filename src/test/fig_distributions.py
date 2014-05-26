from helpers.datahandler import DataHandler
import numpy as np
import matplotlib.pyplot as plt


handler = DataHandler()
genders, ages, diagnoses = handler.getAllData()

# --- Genders distribution ---
# 1 if male
print("Genders distribution")
print(genders.shape[0])
print("Men: {0}".format(sum(genders == 1)))
print("Women: {0}".format(sum(genders == 0)))

# --- Ages distribution ---
print("\nAges distribution")
# create histogram data for age distribution
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
hist, bins = np.histogram(ages, bins=bins)
print("Histogram values:", hist)
print("Bins:", bins)

# plot histogram (just to look at right now; will do it in some other program anyway)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
#plt.bar(center, hist, align='center', width=width)
#plt.show()



# --- Distribution of numbers of diagnoses ---
print("\nDiagnoses distribution")
summed = np.sum(diagnoses, axis=1)
bins = range(0,70,2)
hist, bins = np.histogram(summed, bins=bins)
print("Histogram values:", hist)
print("Bins:", bins)

# plot histogram (just to look at right now; will do it in some other program anyway)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()