import pandas as pd
import numpy as np

# Read dataset in form of CSV files
df = pd.read_csv("C:/Users/Aryansid/Downloads/penguins_DataSet_exam.csv")
missing_data = df.isnull().any()
print(missing_data.head(20))

