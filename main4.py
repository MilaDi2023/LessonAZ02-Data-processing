# Тема - Выбросы (т.е. экстремальные значения в наборах данных)

import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)

# Визуализация 1 в виде гистограммы, где хорошо виден выброс
# df['value'].hist()

# Визуализация 2, где тоже хорошо виден выброс
# df.boxplot(column='value')

# plt.show()

print(df.describe())

Q1 = df['value'].quantile(0.25) # первый квантиль
Q3 = df['value'].quantile(0.75) # третий квантиль
IQR = Q3 - Q1 # межквартальный размах

downside = Q1 - 1.5*IQR # вычисление нижней границы
upperside = Q3 + 1.5*IQR # вычисление верхней границы

# Удаление выброса, который не попал в промежуток между downside и upperside
# Создаем новый датафрейм, у которого все значения входят в промежуток между downside и upperside
df_new = df[(df['value'] >= downside) & (df['value'] <= upperside)]
df_new.boxplot(column='value')
plt.show()


