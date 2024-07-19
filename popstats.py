#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 12, 2023
#This program makes tells me the population in a borough!

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Give me a borough: ") #inputboough

pop = pd.read_csv( 'nycHistPop.csv' ,skiprows=5)#nychist,skip

print(f"Average population: {pop[borough].mean()}")
print(f"Max population: {pop[borough].max()}")