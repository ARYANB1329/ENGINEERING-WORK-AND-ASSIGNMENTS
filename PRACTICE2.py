import pandas as pd
import numpy as np
# Read dataset in form of CSV files
df = pd.read_csv("C:/Users/Aryansid/Downloads/winequality_dataset.csv")
# Replacing Null/Empty Values with mean
mean = df["density"].mean()
k = df["density"].replace(np.nan, mean)
print(k.head(20))


