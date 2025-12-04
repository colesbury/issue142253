import numpy as np

d = np.int32
for i in range(100000):
    d = (d, (1,))

try:
    np.dtype(d)
except RecursionError as exc:
    print(f"RecursionError caught: {exc}")
else:
    raise RuntimeError("no recursion error")
