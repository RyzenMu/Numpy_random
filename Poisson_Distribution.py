# poisson distribution is a Discrete distribution

# It estimates how many times an event can happen in a specified time.

# lam - rate or known number of occurances
# size - The shape of the returned array

import numpy as np

poisson_numbers = np.random.poisson(lam=2, size=10)

print(poisson_numbers)
print('------------------------------------')

#Visualization of Poisson Distribution

import matplotlib.pyplot as plt
import seaborn as sns

poisson_numbers = np.random.poisson(lam=15, size=1000)

sns.distplot(poisson_numbers, kde=False)

plt.show()

print('---------------------------------------')

# Difference between Normal and Poisson Distribution

normal_numbers = np.random.normal(loc=50, scale=7, size=1000)
poisson_numbers = np.random.poisson(lam=50, size=1000)

sns.distplot(normal_numbers, hist=False, label='normal')
sns.distplot(poisson_numbers, hist=False, label='poisson')

plt.legend()
plt.show()

print('------------------------------------------------')

# Difference between Poisson and Binomial Distribution

binomial_numbers = np.random.binomial(n=1000, p=0.01, size=1000)
poisson_numbers = np.random.poisson(lam=10, size=1000)

sns.distplot(binomial_numbers, hist=False, label='binomial')
sns.distplot(poisson_numbers, hist=False, label='poisson')

plt.legend()
plt.show()

print('------------------------------------------------')