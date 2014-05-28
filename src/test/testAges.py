import numpy as np
import matplotlib.pyplot as plt
from helpers.age import Age

ages = np.load('../../data/ages_train.npy')

# print min, max
print(np.min(ages))
print(np.max(ages))

# create histogram data for age distribution
binEdges = [0, 20, 30, 40, 50, 60, 70, 80, 100]
hist, bins = np.histogram(ages, bins=binEdges)
print(hist)

# plot histogram
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()


a = Age()
print(a.agesToBins)
print(a.getBinFromAge(90))