# Plot a Regression plot using ‘mpg’ dataset

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(color_codes=True)
df = pd.read_csv("C:/Users/Aryansid/Downloads/archive/auto-mpg.csv")
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)
sns.regplot(x="mpg", y="weight", data=df)
print(df)
plt.title('Regression Plot between mpg and weight')
# Set x-axis label
plt.xlabel('mpg')
# Set y-axis label
plt.ylabel('weight')
plt.show()


