# random distribution
# creating a 1D array using random and choice
import numpy as np

random_matrix = np.random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0.0], size=(100))

print(random_matrix)