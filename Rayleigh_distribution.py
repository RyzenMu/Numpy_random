# Rayleigh distribution is used in signal processing

# it has two parameters: scale - standard deviation decides how flat the distribution will be default 1.0

# size - The shape of the returned array

import numpy as np

# Draw out a sample rayleigh distribution with scale of 2 with size 2*3:

rayleigh_numbers = np.random.rayleigh(scale=2, size=(2, 3))

print(rayleigh_numbers)

print('-----------------------------------------------------------')

import matplotlib.pyplot as plt
import seaborn as sns

rayleigh_numbers = np.random.rayleigh(scale=33, size=1000)
sns.distplot(rayleigh_numbers, hist=False)
plt.show()

print('----------------------------------------------------------')