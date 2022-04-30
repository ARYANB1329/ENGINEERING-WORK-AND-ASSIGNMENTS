# Draw a Box Plot using seaborn library for the iris dataset
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
sns.set_style("whitegrid")
sns.boxplot(data=iris)
plt.show()

