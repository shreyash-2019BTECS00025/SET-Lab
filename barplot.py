# This python code will display a barplot for given dataset
import pandas as pd
df = pd.read_csv('D:\TY\SET\Assignment1\Toyota.csv')
df.plot(x="FuelType")
