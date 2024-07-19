#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 12, 2023
#This program makes tells me the shelter census!

import pandas as pd
import matplotlib.pyplot as plt

x = input("give me file name")
y = input("give me final file name")

homeless = pd.read_csv(x)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
fig = plt.savefig(y)
