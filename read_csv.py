import pandas as pd

csv_file_paths = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

df3 = []

for csv_files in csv_file_paths:
    df = pd.read_csv(csv_files)
    df3.append(df)

# Combining all three to one dataframe
df = pd.concat(df3)
# print(df.describe())

# Only getting the pink morsels
df = df[df['product'] == 'pink morsel']

# Multiplying price and quantity column
df['sales'] = df['quantity']*df['price'].apply(lambda x: float(x.replace('$', '')))
# print(df.head())

# Final File containing 'region', 'date', 'sales'
task_2_final = df[['sales', 'date', 'region']]

# print(task_2_final)
task_2_final.to_csv('task2.csv', index=False)
