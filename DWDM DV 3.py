import matplotlib.pyplot as plt
Girls = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
Boys = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(grades_range, Girls, color='r')
plt.scatter(grades_range, Boys, color='b')
plt.xlabel('Grades range')
plt.ylabel('Grades Scored')
plt.legend(["Girls", "Boys"], loc ="upper right")
plt.title('SCATTER PLOT')
plt.show()



