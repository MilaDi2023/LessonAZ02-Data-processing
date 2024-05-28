# Тема - Работа с категориальными данными в Pandas

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

# Создаем датафрейм на основе имеющегося словаря
df = pd.DataFrame(data)

# Создаем категорию по гендеру
df['gender'] = df['gender'].astype('category')
print(df['gender'].cat.categories)

# Создаем категорию по департаменту
df['department'] = df['department'].astype('category')
print(df['department'].cat.categories)

# Преобразование категории в числовой код
print(df['gender'].cat.codes)

# Добавление новой категории Finance
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

# Удаление категории HR
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)