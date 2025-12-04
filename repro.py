import numpy as np

d = np.int32
for i in range(100000):
    d = (d, (1,))

np.dtype(d)
print("OK")
