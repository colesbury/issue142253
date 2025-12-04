import numpy as np

d = np.int32
for i in range(100000):
    d = (d, (1,))

try:
    np.dtype(d)
except RecursionError:
    pass
else:
    raise RuntimeError("no recursion error")
