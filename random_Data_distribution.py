# random distribution
# creating a 1D array using random and choice
import numpy as np

random_matrix = np.random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0.0], size=(100))

print(random_matrix)
print('------------------------------------------------------')

# creating a 2D array using random and choice

random_2D_matrix = np.random.choice([3, 4, 6, 9], p=[0.2, 0.5, 0.3, 0.0], size=(3, 5))
print(random_2D_matrix)

print('----------------------------------------------------------------------------------')