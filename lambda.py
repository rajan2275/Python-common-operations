import functools as ft
import pandas as pd

# -------------------
# Example of lambda
# -------------------
mx = lambda x, y: x + y if x > y  else y * x
print(mx(4, 5))

# -------------------
# Example of map
# -------------------
s = pd.Series([1, 2, 3, 4])
print(list(map(lambda x: 3*x, s)))

# -------------------
# Example of filter
# -------------------
s = pd.Series([1, 2, 3, 4])
print(list(filter(lambda x:x > 2, s)))

# -------------------
# Example of reduce
# -------------------
s = pd.Series([1, 2, 3, 4])
print(ft.reduce(lambda x, y: x * y, s))


