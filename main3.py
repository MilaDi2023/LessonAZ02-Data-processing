# Тема - Временные ряды

import pandas as pd
import numpy as np

dates = pd.date_range(start="2022-07-26", periods=10, freq="D") # Промежуток - 1 день

values = np.random.rand(10)

df = pd.DataFrame({'Date': dates, 'Value': values})

# Установим дату как индекс
df.set_index('Date', inplace=True)

print(df)

# Делаем ресемплирование временного ряда. Меняем промежуток с 1 дня на 1 месяц
month = df.resample('M').mean() # с выдачей среднего значения

print()
print(month)