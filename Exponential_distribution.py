# Exponential distribution is used for describing time till next event e.g. failure/sucess etc

# it has two parameters scale- inverse of rate , defaults to 1.0
# size - The shape of the returned array

# draw out a sample for exponential distribution with 2.0 scale with 2*3 size:

import numpy as np

exponential_distribution = np.random.exponential(scale=2, size=(2, 3))

print(exponential_distribution)

print('------------------------------------------------------')

import matplotlib.pyplot as plt
import seaborn as sns

exponential_distribution = np.random.exponential(size=1000)

sns.distplot(exponential_distribution, hist=False)
plt.show()

print('---------------------------------------------------------')