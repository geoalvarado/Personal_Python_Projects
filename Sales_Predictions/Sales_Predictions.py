# The intent of this script is to create a ML model to predict when a specific product needs to be ordered in which part of the month or year.
import pandas as pd
import numpy as np
import sklearn # Use ML to predict date when a certain product should be bought

filename = "/Users/geovanniealvarado/Documents/Personal_Proyects/ML_Practice/Sales/10041_02102025_invoice_82181867_877531.xlsx"
df1 = pd.read_excel(filename, skiprows=17)
df1 = df1.iloc[:-6]

# Need to figure out a way to pull the date when each product is ordered

print('Debug')