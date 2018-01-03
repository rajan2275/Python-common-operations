import pandas as pd
import numpy as np

# ------------------------
# Creating Empty DataFrame
# ------------------------
df = pd.DataFrame()
print(df)
print('----------------------------------')
# ----------------------------
# Creating DataFrame From Lists
# ----------------------------
print('Creating DataFrame From Lists')
print('----------------------------------')

df = pd.DataFrame(data =[['Employee1', 1000],['Employee2', 2000],['Employee3', 4000]],
                  columns=['Name', 'Salary'])
print(df)
print('----------------------------------')

# ----------------------------------
# Creating DataFrame From Dictionary
# ----------------------------------
print('Creating DataFrame From Dictionary')
print('----------------------------------')
data = {'Name': ['Employee1','Employee2', 'Employee3'], 'Salary':[1000, 2000, 3000]}
df = pd.DataFrame(data)
print(df)
print('----------------------------------')

# -------------------
# DataFrame
# -------------------
print('Describe DataFrame')
print('----------------------------------')
print(df.describe())
print('----------------------------------')
print('head function DataFrame')
print('----------------------------------')
print(df.head(1))
print('----------------------------------')
print('tail function DataFrame')
print('----------------------------------')
print(df.tail(1))
print('----------------------------------')




