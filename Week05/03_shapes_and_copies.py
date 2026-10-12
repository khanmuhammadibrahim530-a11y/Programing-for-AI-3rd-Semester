import numpy as np

original = np.array([10, 20, 30, 40, 50])
independent = original[1:4].copy()
independent[0] = 100
print(original)

view = original[1:4]
view[0] = 999
print(original)