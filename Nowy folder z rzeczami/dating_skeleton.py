import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Create your df here:

df = pd.read_csv('/Users/wiktor.fedun/Desktop/capstone_starter/profiles.csv')

print(df.head())
print(df.columns)

#plt.scatter((df.groupby(df["orientation"]).count())["status"])
a = plt.figure(1)
df.orientation.groupby(df["orientation"]).count().plot()
#print((df.groupby(df["orientation"]).count())["status"][:1])
b = plt.figure(2)

plt2 = df.orientation.groupby(df["sex"]).count().plot()
plt.show()
