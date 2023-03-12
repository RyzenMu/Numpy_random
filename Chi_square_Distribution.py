# Chi square distribution is used as a basis to verify the hypothesis

# it has two parameters

# df - degree of freedom and size = The shape of the returned array.

import numpy as np

# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2*3

chi_square_numbers = np.random.chisquare(df=2, size=(2, 3))

print(chi_square_numbers)

print('-------------------------------------------------------')

# Visualization of chi square numbers

import matplotlib.pyplot as plt
import seaborn as sns

chi_square_numbers = np.random.chisquare(df=2, size=1000)
sns.distplot(chi_square_numbers, hist=False)

plt.show()

print('--------------------------------------------------------')
