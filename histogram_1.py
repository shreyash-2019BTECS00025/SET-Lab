import pandas as pd
df = pd.read_csv('D:\TY\SET\Assignment1\Toyota.csv')
df['CC'].plot(kind='hist')