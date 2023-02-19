# Binomial distribution is a Discrete Distribution

# Discrete distribution is defined at separate set of evebts, e.g. coin toss
# whereas height of people is continous as it can be 170, 170.1, 170.11 and so on

# n - number of trials
# p - probability of occurance of each trial
# size - The shape of the returned array

import numpy as np

random_binomial_numbers = np.random.binomial(n=100, p=0.5, size=10)

print(random_binomial_numbers)
print('---------------------------------------------')

# Visualization of Binomial Distribution
import matplotlib.pyplot as plt
import seaborn as sns

random_binomial_numbers = np.random.binomial(n=10, p=0.54, size=1000)
sns.distplot(random_binomial_numbers, hist=True, kde=False)
plt.show()
print('-----------------------------------------------')

# Normal distribution is similar to Binomial distribution with certain loc and scale

random_normal_numbers = np.random.normal(loc=50, scale=5, size=1000)
random_binomial_numbers = np.random.binomial(n=100, p=0.5, size=1000)

sns.distplot(random_normal_numbers, hist=False, label='normal')
sns.distplot(random_binomial_numbers, hist=False, label='binomial')
plt.legend()
plt.show()
print('----------------------.......-------------------------------------')
