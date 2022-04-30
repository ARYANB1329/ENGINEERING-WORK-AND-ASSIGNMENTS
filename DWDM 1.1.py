import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=[' sepal_length', 'sepal _width',
                                                  'petal_length', 'petal_width'])
print(iris_data)
iris_target = pd.DataFrame(data=iris.target, columns=['species'])
iris_df = pd.concat([iris_data, iris_target], axis=1)
print(iris_df)
iris_df['species_name'] = np.where(iris_df['species'] == 0, 'Setosa', None)
iris_df['species_name'] = np.where(iris_df['species'] == 1, 'Versicolor', iris_df['species_name'])
iris_df['species_name'] = np.where(iris_df['species'] == 2, 'Virginica', iris_df['species_name'])

setosa_petal_length = iris_df[iris_df['species_name'] == 'Setosa']['petal_length']
versicolor_petal_length = iris_df[iris_df['species_name'] == 'Versicolor']['petal_length']
virginica_petal_length = iris_df[iris_df['species_name'] == 'Virginica']['petal_length']
fig, ax = plt.subplots(figsize=(12, 7))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('none')
ax.grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)
ax.set_title('Distribution of petal length by species')
dataset = [setosa_petal_length, versicolor_petal_length, virginica_petal_length]
labels = iris_df['species_name'].unique()
ax.boxplot(dataset, labels=labels)
plt.show()
