#Date:  November 2023
#Logical expressions for a 4-bit incrementer

out1 = ...
out2 = ...
out3 = ..

import pandas as pd

csvFile = input('Enter CSV file name: ')
parameter = input("Give me attribute. ")

tickets = pd.read_csv(csvFile)
print("The 10 worst offenders are:")
print(tickets[parameter].value_counts()[:10])