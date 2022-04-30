import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:/Users/Aryansid/Downloads/DBMS_CE_marks.csv")
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)
z = df['Final_Marks_B5']
z1 = df['Final_Marks_B7']
plt.subplot(2, 1, 1)
plt.hist(z, edgecolor="yellow")
plt.ylim(ymin=0, ymax=25)
plt.xlim(xmin=25, xmax=38)
plt.title('B5 MARKS')
plt.subplot(2, 1, 2)
plt.hist(z1, edgecolor="yellow")
plt.title('B7 MARKS')
plt.ylim(ymin=0, ymax=50)
plt.xlim(xmin=0, xmax=40)
print(df)
plt.show()



