# This program will display a histogram for given dataset
import pandas as pd
df = pd.read_csv('D:\TY\SET\Assignment1\Toyota.csv')
df.plot(x="KM", y="CC")
