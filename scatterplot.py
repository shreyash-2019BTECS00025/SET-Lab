#This python code will display a scatterplot for given dataset
import pandas as pd
df = pd.read_csv('D:/TY/SET/Assignment1/Toyota.csv')
df.plot.scatter(x="Age", y="Price")